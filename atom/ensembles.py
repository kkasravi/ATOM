# -*- coding: utf-8 -*-

"""
Automated Tool for Optimized Modelling (ATOM)
Author: Mavs
Description: Module containing the ensemble estimators.

"""

# Standard packages
import numpy as np
from copy import deepcopy
from joblib import Parallel, delayed

# Sklearn
from sklearn.base import clone
from sklearn.utils import Bunch
from sklearn.base import is_classifier
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import (
    VotingClassifier as VC,
    VotingRegressor as VR,
    StackingClassifier as SC,
    StackingRegressor as SR,
)
from sklearn.utils.validation import column_or_1d
from sklearn.ensemble._base import _fit_single_estimator
from sklearn.model_selection import check_cv, cross_val_predict
from sklearn.utils.multiclass import check_classification_targets

# Own modules
from .utils import check_is_fitted


class BaseEnsemble:
    """Base class for all ensemble estimators."""

    def _get_fitted_attrs(self):
        """Update the fitted attributes (end with underscore)"""
        self.named_estimators_ = Bunch()

        # Uses 'drop' as placeholder for dropped estimators
        est_iter = iter(self.estimators_)
        for name, est in self.estimators:
            if est == "drop" or check_is_fitted(est, False):
                self.named_estimators_[name] = est
            else:
                self.named_estimators_[name] = next(est_iter)

            if hasattr(est, "feature_names_in_"):
                self.feature_names_in_ = est.feature_names_in_


class BaseVoting(BaseEnsemble):
    """Base class for the voting estimators."""

    def fit(self, X, y, sample_weight=None):
        names, all_estimators = self._validate_estimators()

        # Difference with sklearn's implementation, skip fitted estimators
        estimators = Parallel(n_jobs=self.n_jobs)(
            delayed(_fit_single_estimator)(
                clone(clf),
                X,
                y,
                sample_weight=sample_weight,
                message_clsname="Voting",
                message=self._log_message(names[idx], idx + 1, len(all_estimators)),
            )
            for idx, clf in enumerate(all_estimators)
            if clf != "drop" and not check_is_fitted(clf, False)
        )

        self.estimators_ = []
        estimators = iter(estimators)
        for est in self.estimators:
            if est[1] != "drop":
                if check_is_fitted(est[1], False):
                    self.estimators_.append(est[1])
                else:
                    self.estimators_.append(next(estimators))

        self._get_fitted_attrs()  # Update the fit attrs

        return self


class BaseStacking(BaseEnsemble):
    """Base class for the stacking estimators."""

    def fit(self, X, y, sample_weight=None):
        names, all_estimators = self._validate_estimators()
        self._validate_final_estimator()

        stack_method = [self.stack_method] * len(all_estimators)

        # Difference with sklearn's implementation, skip fitted estimators
        estimators = Parallel(n_jobs=self.n_jobs)(
            delayed(_fit_single_estimator)(clone(clf), X, y, sample_weight)
            for idx, clf in enumerate(all_estimators)
            if clf != "drop" and not check_is_fitted(clf, False)
        )

        self.estimators_ = []
        estimators = iter(estimators)
        for est in self.estimators:
            if est[1] != "drop":
                if check_is_fitted(est[1], False):
                    self.estimators_.append(est[1])
                else:
                    self.estimators_.append(next(estimators))

        self._get_fitted_attrs()  # Update the fit attrs

        # To train the meta-classifier using the most data as possible,
        # we use cross-validation for the output of the stacked estimators

        # To ensure that the data provided to each estimator are the
        # same, we need to set the random state of the cv if there is
        # one and we need to take a copy
        cv = check_cv(self.cv, y=y, classifier=is_classifier(self))
        if hasattr(cv, "random_state") and cv.random_state is None:
            cv.random_state = np.random.RandomState()

        self.stack_method_ = [
            self._method_name(name, est, meth)
            for name, est, meth in zip(names, all_estimators, stack_method)
        ]
        fit_params = (
            {"sample_weight": sample_weight} if sample_weight is not None else None
        )

        predictions = Parallel(n_jobs=self.n_jobs)(
            delayed(cross_val_predict)(
                clone(est),
                X,
                y,
                cv=deepcopy(cv),
                method=meth,
                n_jobs=self.n_jobs,
                fit_params=fit_params,
                verbose=self.verbose,
            )
            for est, meth in zip(all_estimators, self.stack_method_)
            if est != "drop"
        )

        # Only not None or not 'drop' estimators will be used in transform.
        # Remove the None from the method as well.
        self.stack_method_ = [
            meth for (meth, est) in zip(self.stack_method_, all_estimators)
            if est != "drop"
        ]

        X_meta = self._concatenate_predictions(X, predictions)
        _fit_single_estimator(
            self.final_estimator_, X_meta, y, sample_weight=sample_weight
        )

        return self


class VotingClassifier(BaseVoting, VC):
    """Soft Voting/Majority Rule classifier.

    Modified version of sklearn's VotingClassifier. Differences are:
        - Doesn't fit estimators if they're already fitted.
        - Is considered fitted when all estimators are at initialization.
        - Doesn't implement a LabelEncoder to encode the target column.

    """

    def __init__(
            self,
            estimators,
            *,
            voting="hard",
            weights=None,
            n_jobs=None,
            flatten_transform=True,
            verbose=False,
    ):
        super().__init__(
            estimators,
            voting=voting,
            weights=weights,
            n_jobs=n_jobs,
            flatten_transform=flatten_transform,
            verbose=verbose,
        )

        # If all estimators are prefit, create fitted attrs
        if all(e[1] == "drop" or check_is_fitted(e[1], False) for e in self.estimators):
            self.estimators_ = [e[1] for e in self.estimators if e[1] != "drop"]
            self._get_fitted_attrs()

    def fit(self, X, y, sample_weight=None):
        """Fit the estimators, skipping prefit ones.

        Parameters
        ----------
        X: {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vectors, where `n_samples` is the number of
            samples and `n_features` is the number of features.

        y: array-like of shape (n_samples,)
            Target values.

        sample_weight: array-like of shape (n_samples,), default=None
            Sample weights. If None, then samples are equally weighted.
            Note that this is supported only if all underlying estimators
            support sample weights.

        Returns
        -------
        self: VotingClassifier
            Fitted instance of self.

        """
        check_classification_targets(y)
        if isinstance(y, np.ndarray) and len(y.shape) > 1 and y.shape[1] > 1:
            raise NotImplementedError(
                "Multilabel and multi-output classification is not supported."
            )

        if self.voting not in ("soft", "hard"):
            raise ValueError(
                f"Voting must be 'soft' or 'hard', got (voting={self.voting})."
            )

        if self.weights is not None and len(self.weights) != len(self.estimators):
            raise ValueError(
                "Number of estimators and weights must be equal, got "
                f"{len(self.weights)} weights, {len(self.estimators)} estimators."
            )

        return super().fit(X, y, sample_weight)

    def predict(self, X):
        """Predict class labels for X.

        Parameters
        ----------
        X: {array-like, sparse matrix} of shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        predictions: array-like of shape (n_samples,)
            Predicted class labels.

        """
        check_is_fitted(self)
        if self.voting == "soft":
            return np.argmax(self.predict_proba(X), axis=1)
        else:
            return np.apply_along_axis(
                lambda x: np.argmax(np.bincount(x, weights=self._weights_not_none)),
                axis=1,
                arr=self._predict(X),
            )


class VotingRegressor(BaseVoting, VR):
    """Soft Voting/Majority Rule regressor.

    Modified version of sklearn's VotingRegressor. Differences are:
        - Doesn't fit estimators if they're already fitted.
        - Is considered fitted when all estimators are at initialization.

    """

    def __init__(self, estimators, *, weights=None, n_jobs=None, verbose=False):
        super().__init__(
            estimators,
            weights=weights,
            n_jobs=n_jobs,
            verbose=verbose,
        )

        # If all estimators are prefit, create fitted attrs
        if all(e[1] == "drop" or check_is_fitted(e[1], False) for e in self.estimators):
            self.estimators_ = [est[1] for est in self.estimators if est[1] != "drop"]
            self._get_fitted_attrs()


class StackingClassifier(BaseStacking, SC):
    """Stack of estimators with a final classifier.

    Modified version of sklearn's StackingClassifier. Difference is:
        - Doesn't fit estimators if they're already fitted.

    """

    def fit(self, X, y, sample_weight=None):
        """Fit the estimators, skipping prefit ones.

        Parameters
        ----------
        X: {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vectors, where `n_samples` is the number of
            samples and `n_features` is the number of features.

        y: array-like of shape (n_samples,)
            Target values.

        sample_weight: array-like of shape (n_samples,), default=None
            Sample weights. If None, then samples are equally weighted.
            Note that this is supported only if all underlying estimators
            support sample weights.

        Returns
        -------
        self: StackingClassifier
            Fitted instance of self.

        """
        check_classification_targets(y)
        self._le = LabelEncoder().fit(y)
        self.classes_ = self._le.classes_
        return super().fit(X, self._le.transform(y), sample_weight)


class StackingRegressor(BaseStacking, SR):
    """Stack of estimators with a final regressor.

    Modified version of sklearn's StackingRegressor. Difference is:
        - Doesn't fit estimators if they're already fitted.

    """

    def fit(self, X, y, sample_weight=None):
        """Fit the estimators, skipping prefit ones.

        Parameters
        ----------
        X: {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vectors, where `n_samples` is the number of
            samples and `n_features` is the number of features.

        y: array-like of shape (n_samples,)
            Target values.

        sample_weight: array-like of shape (n_samples,), default=None
            Sample weights. If None, then samples are equally weighted.
            Note that this is supported only if all underlying estimators
            support sample weights.

        Returns
        -------
        self: StackingRegressor
            Fitted instance of self.

        """
        y = column_or_1d(y, warn=True)
        return super().fit(X, y, sample_weight)
