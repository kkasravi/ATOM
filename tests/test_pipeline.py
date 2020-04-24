# coding: utf-8

"""
Automated Tool for Optimized Modelling (ATOM)
Author: tvdboom
Description: Unit tests for the fit method of the ATOM class.

"""

# Import packages
import pytest
import numpy as np
import pandas as pd
from sklearn.metrics import get_scorer, f1_score
from sklearn.datasets import load_breast_cancer, load_wine, load_boston
from atom import ATOMClassifier, ATOMRegressor


# << ====================== Variables ====================== >>

X_dim4 = [[2, 0, 1], [2, 3, 4], [5, 2, 7], [8, 9, 10]]
y_dim4_class = [0, 1, 1, 0]
y_dim4_reg = [1, 2, 4, 3]
X_bin, y_bin = load_breast_cancer(return_X_y=True)
X_class, y_class = load_wine(return_X_y=True)
X_reg, y_reg = load_boston(return_X_y=True)


# << ======================= Tests ========================= >>

# << =================== Test parameters =================== >>

def test_models_parameter():
    """ Assert that the models parameter is set correctly """

    # Raises error when unknown, wrong or duplicate models
    atom = ATOMClassifier(X_dim4, y_dim4_class)
    pytest.raises(ValueError, atom.pipeline, models='test')
    pytest.raises(ValueError, atom.pipeline, models='OLS')
    pytest.raises(ValueError, atom.pipeline, models=['lda', 'lda'])

    atom = ATOMRegressor(X_dim4, y_dim4_reg)
    pytest.raises(ValueError, atom.pipeline, models='lda', metric='r2')

    # Makes it a list
    atom = ATOMClassifier(X_bin, y_bin)
    atom.pipeline('lr', 'precision', max_iter=0)
    assert isinstance(atom.models, list)


def test_metric_parameter():
    """ Assert that the metric parameter is set correctly """

    # Test default metrics
    atom = ATOMClassifier(X_bin, y_bin)
    atom.pipeline('lr')
    assert atom.metric.name == 'f1'

    atom = ATOMClassifier(X_class, y_class)
    atom.pipeline('lr')
    assert atom.metric.name == 'f1_weighted'

    atom = ATOMRegressor(X_reg, y_reg)
    atom.pipeline('ols')
    assert atom.metric.name == 'r2'

    # Test unknown metric
    atom = ATOMClassifier(X_dim4, y_dim4_class)
    pytest.raises(ValueError, atom.pipeline, models='lda', metric='unknown')

    # Test custom metric
    def metric_func(x, y):
        return x, y
    pytest.raises(ValueError, atom.pipeline, models='lda', metric=metric_func)

    atom.pipeline('lr', metric=f1_score)
    assert 1 == 1

    # Test scoring metric
    atom = ATOMRegressor(X_dim4, y_dim4_reg)
    scorer = get_scorer('neg_mean_squared_error')
    atom.pipeline('ols', metric=scorer)
    assert 2 == 2

    # Test same metric as last run
    atom = ATOMRegressor(X_dim4, y_dim4_reg)
    atom.pipeline('ols', metric='max_error')
    atom.pipeline('br')
    assert atom.metric.name == 'max_error'


def test_skip_iter_parameter():
    """ Assert that the skip_iter parameter is set correctly """

    atom = ATOMClassifier(X_dim4, y_dim4_class)
    pytest.raises(ValueError, atom.successive_halving, 'lda', skip_iter=-2)


def test_max_iter_parameter():
    """ Assert that the max_iter parameter is set correctly """

    atom = ATOMClassifier(X_dim4, y_dim4_class)
    pytest.raises(ValueError, atom.pipeline, 'lda', 'f1', max_iter=-2)
    pytest.raises(ValueError, atom.pipeline, 'lda', 'f1', max_iter=[2, 2])


def test_max_time_parameter():
    """ Assert that the max_time parameter is set correctly """

    atom = ATOMClassifier(X_dim4, y_dim4_class)
    pytest.raises(ValueError, atom.pipeline, 'lda', 'f1', max_time=-2)
    pytest.raises(ValueError, atom.pipeline, 'lda', 'f1', max_time=[2, 2])


def test_init_points_parameter():
    """ Assert that the init_points parameter is set correctly """

    atom = ATOMClassifier(X_dim4, y_dim4_class)
    pytest.raises(ValueError, atom.pipeline, 'lda', 'f1', init_points=-2)
    pytest.raises(ValueError, atom.pipeline, 'lda', 'f1', init_points=[2, 2])


def test_cv_parameter():
    """ Assert that the cv parameter is set correctly """

    atom = ATOMClassifier(X_dim4, y_dim4_class)
    pytest.raises(ValueError, atom.pipeline, 'lda', 'f1', cv=-2)
    pytest.raises(ValueError, atom.pipeline, 'lda', 'f1', cv=[2, 2])


def test_bagging_parameter():
    """ Assert that the bagging parameter is set correctly """

    atom = ATOMClassifier(X_dim4, y_dim4_class)
    pytest.raises(ValueError, atom.pipeline, 'lda', 'f1', bagging=-2)


# << ================== Test pipelines ================= >>

def test_data_preparation():
    """ Assert that the data_preparation function works as intended """

    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.pipeline(models='lgb')
    assert atom.X_train_scaled.iloc[:, 1].mean() < 0.05
    assert atom.X_test_scaled.iloc[:, 0].std() < 1.25


def test_successive_halving():
    """ Assert that the successive_halving method works as intended """

    # Without bagging
    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.successive_halving(models=['tree', 'rf', 'xgb', 'lgb'],
                            metric='f1',
                            max_iter=0,
                            bagging=0)
    assert isinstance(atom.scores, list)
    assert len(atom.scores) == 3

    # With bagging
    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.successive_halving(models=['tree', 'rf', 'xgb', 'lgb'],
                            metric='f1',
                            max_iter=0,
                            bagging=5)
    assert isinstance(atom.scores, list)
    assert len(atom.scores) == 3


def test_skip_iter_scores():
    """ Assert that self.scores is correctly created when skip_iter > 0 """

    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.successive_halving(models=['tree', 'rf', 'xgb', 'lgb'],
                            metric='f1',
                            skip_iter=1,
                            max_iter=0)
    assert isinstance(atom.scores, list)
    assert len(atom.scores) == 2


def test_train_sizing():
    """ Assert that the train_sizing method works as intended """

    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.train_sizing(models=['tree', 'rf', 'xgb', 'lgb'],
                      metric='f1',
                      max_iter=0,
                      bagging=5)
    assert isinstance(atom.scores, list)
    assert len(atom.scores) == 10


def test_errors_in_models():
    """ Assert that errors when running models are handled correctly """

    atom = ATOMRegressor(X_reg, y_reg, random_state=1)
    atom.X.iloc[2, 3] = np.NaN  # Make it fail
    atom.update('X')
    atom.pipeline(models=['Tree', 'XGB'],
                  metric='neg_mean_squared_log_error',
                  max_iter=0)
    assert 'Tree' in atom.errors.keys()
    assert 'Tree' not in atom.models


def test_lower_case_model_attribute():
    """ Assert that model attributes can be called with lowercase as well """

    atom = ATOMClassifier(X_dim4, y_dim4_class,
                          random_state=1, verbose=1)  # vb=1 for coverage :D
    atom.pipeline(models='tree', metric='f1', max_iter=0)
    assert atom.Tree == atom.tree


def test_plot_bo():
    """ Assert that plot_bo works as intended """

    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.pipeline('tree', 'f1',  max_iter=15, init_points=10, plot_bo=True)
    assert 1 == 1


def test_different_cv_values():
    """ Assert that changing the cv parameter works as intended """

    # For classification
    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.pipeline(models='pa', metric='roc_auc', max_iter=5, cv=3)
    assert 1 == 1

    # For regression
    atom = ATOMRegressor(X_reg, y_reg, random_state=1)
    atom.pipeline(models='tree', metric='r2', max_iter=5, cv=3)
    assert 2 == 2


def test_model_attributes():
    """ Assert that the model subclass has all attributes set """

    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.pipeline(models=['tree', 'pa'], max_iter=2)
    assert 'params' in atom.Tree.BO.keys()
    assert 'score' in atom.Tree.BO.keys()
    assert 'time' in atom.Tree.BO.keys()
    assert 'total_time' in atom.Tree.BO.keys()
    assert hasattr(atom.Tree, 'best_params')
    assert hasattr(atom.PA, 'best_model')
    assert hasattr(atom.Tree, 'best_model_fit')
    assert hasattr(atom.Tree, 'predict_train')
    assert hasattr(atom.pa, 'predict_test')
    assert hasattr(atom.Tree, 'predict_proba_train')
    assert hasattr(atom.Tree, 'predict_proba_test')
    assert hasattr(atom.PA, 'decision_function_train')
    assert hasattr(atom.PA, 'decision_function_test')
    assert hasattr(atom.Tree, 'score_train')
    assert hasattr(atom.PA, 'score_test')
    assert hasattr(atom.PA, 'confusion_matrix')
    assert hasattr(atom.PA, 'tp')
    assert hasattr(atom.PA, 'fn')


def test_bagging():
    """ Assert that bagging workas as intended """

    # For metric needs proba
    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.pipeline(models=['tree', 'lgb'], max_iter=1, cv=1, bagging=5)
    assert hasattr(atom.Tree, 'bagging_scores')

    # For metric needs proba but hasn't attr
    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.pipeline(models='PA', metric='roc_auc', max_iter=1, cv=1, bagging=5)
    assert hasattr(atom.PA, 'bagging_scores')

    # For metric does not needs proba
    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.pipeline(models='tree', metric='f1', max_iter=1, cv=1, bagging=5)
    assert hasattr(atom.Tree, 'bagging_scores')


def test_winner_attribute():
    """ Assert that the best model is attached to the winner attribute """

    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.pipeline(['lr', 'tree', 'lgb'], 'f1')
    assert atom.winner.name == 'LGB'

    atom = ATOMRegressor(X_reg, y_reg, random_state=1)
    atom.pipeline(['br', 'ols', 'tree'], 'max_error')
    assert atom.winner.name == 'Tree'


# << ================== Test transforming methods ================= >>

def test_transform_method():
    """ Assert that the transform method works as intended """

    X = [[2, 0, 'a'], [2, 3, 'a'], [5, 2, 'b'], [1, 2, 'a'], [1, 2, 'c'],
         [2, 0, 'd'], [2, 3, 'd'], [5, 2, 'd'], [1, 2, 'a'], [1, 2, 'd']]
    y = [0, 1, 0, 1, 1, 0, 1, 0, 1, 1]
    atom = ATOMClassifier(X, y, random_state=1)
    atom.impute(strat_num='median', strat_cat='remove')
    atom.encode(max_onehot=None)
    atom.pipeline('Tree', 'f1')

    # With default arguments
    X_trans = atom.transform(X)
    assert X_trans['Feature 2'].dtype.kind in 'ifu'

    # From model
    X_trans = atom.Tree.transform(X)
    assert X_trans['Feature 2'].dtype.kind in 'ifu'

    # Changing arguments
    X_trans = atom.transform(X, encode=False)
    assert X_trans['Feature 2'].dtype.kind not in 'ifu'


def test_predict_method():
    """ Assert that the predict method works as intended """

    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.outliers(max_sigma=3)

    # Check if error is raised when its not fitted
    pytest.raises(AttributeError, atom.predict, X_bin)

    atom.pipeline('Tree', 'f1')
    predictions1 = atom.predict(X_bin)
    predictions2 = atom.Tree.predict(X_bin)

    # Check if array only consists of 0 and 1
    assert np.array_equal(predictions1, predictions1.astype(bool))
    assert np.array_equal(predictions2, predictions2.astype(bool))


def test_predict_proba_method():
    """ Assert that the predict_proba method works as intended """

    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.outliers(max_sigma=3)
    atom.pipeline('Tree', 'f1')
    predictions1 = atom.predict_proba(X_bin)
    predictions2 = atom.Tree.predict_proba(X_bin)

    # Check if array is 2-dimensional
    assert predictions1.shape[1] == 2
    assert predictions2.shape[1] == 2


def test_predict_log_proba_method():
    """ Assert that the predict_log_proba method works as intended """

    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.outliers(max_sigma=3)
    atom.pipeline('Tree', 'f1')
    predictions1 = atom.predict_log_proba(X_bin)
    predictions2 = atom.Tree.predict_log_proba(X_bin)

    # Check if array is 2-dimensional
    assert predictions1.shape[1] == 2
    assert predictions2.shape[1] == 2


def test_decision_function_method():
    """ Assert that the predict_log_proba method works as intended """

    atom = ATOMClassifier(X_bin, y_bin, random_state=1)
    atom.outliers(max_sigma=3)
    atom.pipeline('Tree', 'f1')

    # When model hasn't got the attribute
    pytest.raises(AttributeError, atom.decision_function, X_bin)
    pytest.raises(AttributeError, atom.Tree.decision_function, X_bin)

    atom.pipeline('lsvm', 'f1')
    predictions1 = atom.decision_function(X_bin)
    predictions2 = atom.lsvm.decision_function(X_bin)

    # Check if array is 2-dimensional
    assert isinstance(predictions1, np.ndarray)
    assert isinstance(predictions2, np.ndarray)
