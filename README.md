<p align="center">
	<img src="https://github.com/tvdboom/ATOM/blob/master/images/logo.png?raw=true" alt="ATOM" title="ATOM" width="500" height="140"/>
</p>

# Automated Tool for Optimized Modelling
Author: tvdboom  
Email: m.524687@gmail.com

[![Python 3.6|3.7](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)](https://www.python.org/downloads/release/python-380/)
[![License: MIT](https://img.shields.io/github/license/tvdboom/ATOM)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/atom-ml)](https://pypi.org/project/atom-ml/)
  
Description  
------------------------  
Automated Tool for Optimized Modelling (ATOM) is a python package designed for fast exploration of supervised machine learning solutions. With just a few lines of code, you can perform basic data cleaning steps, feature selection and compare the performance of multiple models on a given dataset. ATOM should be able to provide quick insights on which algorithms perform best for the task at hand and provide an indication of the feasibility of the machine learning solution. This package supports binary classification, multiclass classification and regression tasks.

| NOTE: A data scientist with knowledge of the data will quickly outperform ATOM if he applies usecase-specific feature engineering or data cleaning methods. Use ATOM only for a fast exploration of the problem! |
| --- |

Possible steps taken by the ATOM pipeline:
1. Data Cleaning
	* Handle missing values
	* Encode categorical features
	* Balance the dataset
	* Remove outliers
2. Perform feature selection
	* Remove features with too high collinearity
	* Remove features with too low variance
	* Select best features according to a chosen strategy
3. Fit all selected models (either direct or via successive halving)
	* Select hyperparameters using a Bayesian Optimization approach
	* Perform bagging to assess the robustness of the model
4. Analyze the results using the provided plotting functions!

<br/><br/>

<p align="center">
	<img src="https://github.com/tvdboom/ATOM/blob/master/images/diagram.png?raw=true" alt="diagram" title="diagram" width="700" height="250" />
</p>


Installation
------------------------  
Intall ATOM easily using `pip`
	
	pip install atom-ml

Usage  
------------------------  
Call the `ATOMClassifier` or `ATOMRegressor` class and provide the data you want to use:  

    from atom import ATOMClassifier  
    
    atom = ATOMClassifier(X, y, log='atom_log', n_jobs=2, verbose=1)

ATOM has multiple data cleaning methods to help you prepare the data for modelling:

    atom.impute(strat_num='knn', strat_cat='most_frequent',  max_frac_rows=0.1)  
    atom.encode(max_onehot=10, frac_to_other=0.05)  
    atom.outliers(max_sigma=4)  
    atom.balance(oversample=0.8, n_neighbors=15)  
    atom.feature_selection(strategy='univariate', solver='chi2', max_features=0.9)

Fit the data to different models:

    atom.fit(models=['LR', 'LDA', 'XGB', 'lSVM'],
	         metric='f1',
	         max_iter=10,
	         max_time=1000,
	         init_points=3,
	         cv=4,
	         bagging=10)  

Make plots and analyze results: 

	atom.plot_bagging(filename='bagging_results.png')  
	atom.lSVM.plot_probabilities()  
	atom.lda.plot_confusion_matrix()  
  

API
-----------------------------
* **ATOMClassifier(X, y=None, percentage=100, test_size=0.3, log=None, n_jobs=1, warnings=False, verbose=0, random_state=None)**  
ATOM class for classification tasks. When initializing the class, ATOM will automatically proceed to apply some standard data cleaning steps unto the data. These steps include transforming the input data into a pd.DataFrame (if it wasn't one already) that can be accessed through the class' attributes, removing columns with prohibited data types, removing categorical columns with maximal cardinality (the number of unique values is equal to the number of instances. Usually the case for IDs, names, etc...), remove features with all the same value, removing duplicate rows and remove rows with missing values in the target column.  
	+ **X: list, np.array or pd.DataFrame**  
	Data features with shape=(n_samples, n_features).
	+ **y: None, string, list, np.array or pd.Series, optional (default=None)**  
		- If None: the last column of X is selected as target column
		- If string: name of the target column in X (X has to be a pd.DataFrame)
		- Else: data target column with shape=(n_samples,)
	+ **percentage: int or float, optional (default=100)**  
	Percentage of the data to use.
	+ **test_size: float, optional (default=0.3)**  
	Split ratio of the train and test set.
	+ **log: None or string, optional (default=None)**  
	Name of the log file. None to not save any log.
	+ **n_jobs: int, optional (default=1)**  
	Number of cores to use for parallel processing.
		+ If -1, use all available cores
		+ If <-1, use available_cores - 1 + n_jobs  
	+ **warnings: bool, optional (default=False)**  
	Wether to show warnings when running the pipeline.
	+ **verbose: int, optional (default=0)**  
	Verbosity level of the class. Possible values are:  
		+ 0 to not print anything  
		+ 1 to print minimum information
		+ 2 to print average information
		+ 3 to print maximum information
	+ **random_state: None or int, optional (default=None)**  
	Seed used by the random number generator. If None, the random number generator is the RandomState instance used by `np.random`.<br><br>
* **ATOMRegressor(X, y=None, target=None, percentage=100, test_size=0.3, log=None, n_jobs=1, warnings=False, verbose=0, random_state=None)**  
ATOM class for regression tasks. See `ATOMClassifier` for an explanation of the class' parameters.


Methods
----------------------------- 
ATOM contains multiple methods for standard data cleaning and feature selection processes. Calling on one of them will automatically apply the method on the dataset in the class and update the class' attributes accordingly.

| TIP: Use the `report` method to examine the data and help you determine suitable parameters for the methods |
| --- |

* **impute(strat_num='remove', strat_cat='remove', max_frac_rows=0.5, max_frac_cols=0.5, missing=[None, np.nan, np.inf, -np.inf, '', '?', 'NA', 'nan', 'inf'])**  
Handle missing values according to the selected strategy. Also removes rows and columns with too many missing values.
	+ **strat_num: int, float or string, optional (default='remove')**  
	Imputing strategy for numerical columns. Possible values are:
		- 'remove': remove row
		- 'mean': impute with mean of column
		- 'median': impute with median of column
		- 'knn': impute using k-Nearest Neighbors
		- 'most_frequent': impute with most frequent value
		- int or float: impute with provided numerical value
	+ **strat_cat: string, optional (default='remove')**  
	Imputing strategy for categorical columns. Possible values are:
		- 'remove': remove row
		- 'most_frequent': impute with most frequent value
		- string: impute with provided string
	+ **max_frac_rows: float, optional (default=0.5)**  
	Minimum fraction of non missing values in row. If less, the row is removed.
	+ **max_frac_cols: float, optional (default=0.5)**  
	Minimum fraction of non missing values in column. If less, the column is removed.
	+ **missing: value or list of values, optional (default=[None, np.nan, np.inf, -np.inf, '', '?', 'NA', 'nan', 'inf'])**  
	List of values to consider as missing. None, np.nan, np.inf and -np.inf are always imputed since they are incompatible with the models.<br><br>
* **encode(max_onehot=10, frac_to_other=0)**  
Perform encoding of categorical features. The encoding type depends on the number of unique values in the column: label-encoding for n_unique=2, one-hot-encoding for 2 < n_unique <= max_onehot and target-encoding for n_unique > max_onehot. It also can replace classes with low occurences with the value 'other' in order to prevent too high cardinality.
	+ **max_onehot: None or int, optional (default=10)**  
	Maximum number of unique values in a feature to perform one-hot-encoding. If None, it will never perform one-hot-encoding.  
	+ **frac_to_other: float, optional (default=0)**  
	Classes with less instances than n_rows * frac_to_other are replaced with 'other'.<br><br>
* **outliers(max_sigma=3, include_target=False)**  
Remove outliers from the training set.
	+ **max_sigma: int or float, optional (default=3)**  
	Remove rows containing any value with a maximum standard deviation (on the respective column) above max_sigma.
	+ **include_target: bool, optional (default=False)**  
	Wether to include the target column when searching for outliers.<br><br>
* **balance(oversample=None, undersample=None, n_neighbors=5)**  
Balance the number of instances per target class. Only for classification tasks. Dependency: [imbalanced-learn](https://imbalanced-learn.readthedocs.io/en/stable/api.html).
	+ **oversample: None, float or string, optional (default=None)**  
	Oversampling strategy using [ADASYN](https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.over_sampling.ADASYN.html#imblearn.over_sampling.ADASYN). Choose from:
		- None: do not perform oversampling
		- float: fraction minority/majority (only for binary classification)
		- 'minority': resample only the minority class
		- 'not minority': resample all but minority class
		- 'not majority': resample all but majority class
		- 'all': resample all classes
	+ **undersample: None, float or string, optional (default=None)**  
	Undersampling strategy using [NearMiss](https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.under_sampling.NearMiss.html) methods. Choose from:
		- None: do not perform undersampling
		- float: fraction minority/majority (only for binary classification)
		- 'majority': resample only the majority class
		- 'not minority': resample all but minority class
		- 'not majority': resample all but majority class
		- 'all': resample all classes
	+ **n_neighbors: int, optional (default=5)**  
	Number of nearest neighbors used for any of the algorithms.<br><br>
* **feature_insertion(n_features=2, generations=20, population=500)**  
Use a genetic algorithm to create new combinations of existing features and add them to the original dataset in order to capture the non-linear relations between the original features. A dataframe containing the description of the newly generated features and their scores can be accessed through the `genetic_features` attribute. The algorithm is implemented using the [Symbolic Transformer](https://gplearn.readthedocs.io/en/stable/reference.html#symbolic-transformer) method, which can be accessed through the `genetic_algorithm` attribute. It is adviced to only use this method when fitting linear models. Dependency: [gplearn](https://gplearn.readthedocs.io/en/stable/index.html).
	+ **n_features: int, optional (default=2)**  
	Maximum number of newly generated features (no more than 1% of the population).
	+ **generations: int, optional (default=20)**  
	Number of generations to evolve.
	+ **population: int, optional (default=500)**  
	Number of entities in each generation.<br><br>
* **feature_selection(strategy=None, solver=None, max_features=None, threshold=-np.inf, frac_variance=1., max_correlation=0.98)**  
Select best features according to the selected strategy. Ties between features with equal scores will be broken in an unspecified way. Also removes features with too low variance and too high collinearity.
	+ **strategy: string, optional (default='univariate')**  
	Feature selection strategy to use. Choose from:
		- None: do not perform any feature selection algorithm (it does still look for multicollinearity and variance)
		- 'univariate': perform a univariate statistical test
		- 'PCA': perform a principal component analysis
		- 'SFM': select best features from an existing model
		- 'RFE': recursive feature eliminator
	+ **solver: string or callable (default=depend on strategy)**  
	Solver or model to use for the feature selection strategy. See the sklearn documentation for an extended descrition of the choices. Select None for the default option per strategy (not applicable for SFM).
		- for 'univariate', choose from:
			* 'f_classif' (default for classification tasks)
			* 'f_regression' (default for regression tasks)
			* 'mutual_info_classif'
			* 'mutual_info_regression'
			* 'chi2'
			* Any function taking two arrays (X, y), and returning arrays (scores, pvalues). See the [documentation](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection).
		- for 'PCA', choose from:
			* 'auto' (default)
			* 'full'
			* 'arpack'
			* 'randomized'
		- for 'SFM': choose a base estimator from which the transformer is built. The estimator must have either a feature_importances_ or coef_ attribute after fitting. This parameter has no default option.
		- for 'RFE': choose a supervised learning estimator. The estimator must have either a feature_importances_ or coef_ attribute after fitting. This parameter has no default option.
	+ **max_features: None, int or float, optional (default=None)**  
	Number of features to select.
		- None: select all features
		- if >= 1: number of features to select
		- if < 1: fraction of features to select
	+ **threshold: string or float, optional (default=-np.inf)**  
	Threshold value to attain when selecting the best features (works only when strategy='SFM'). Features whose importance is greater or equal are kept while the others are discarded.
		- if 'mean': set the mean of feature_importances as threshold
		- if 'median': set the median of feature_importances as threshold
	+ **frac_variance: float, optional (default=1)**  
	Remove features with the same value in at least this fraction of the total. None to skip this step.
	+ **max_correlation: float, optional (default=0.98)**  
	Minimum value of the Pearson correlation cofficient to identify correlated features. A dataframe of the removed features and their correlation values can be accessed through the `collinear` attribute. None to skip this step.<br><br>
* **fit(models, metric, greater_is_better=True, needs_proba=False, successive_halving=False, skip_steps=0, max_iter=15, max_time=np.inf, eps=1e-08, batch_size=1, init_points=5, plot_bo=False, cv=3, bagging=None)**  
Fit class to the selected models. The optimal hyperparameters per model are selectred using a Bayesian Optimization (BO) algorithm with gaussian process as kernel. The resulting score of each step of the BO is either computed by cross-validation on the complete training set or by creating a validation set from the training set. This process will create some minimal leakage but ensures a maximal use of the provided data. The test set, however, does not contain any leakage and will be used to determine the final score of every model. Note that the best score on the BO can be consistently lower than the final score on the test set (despite the leakage) due to the considerable fewer instances on which it is trained. At the end of te pipeline, you can choose to evaluate the robustness of the model's performance on the test set applying a bagging algorithm.
	+ **models: string or list of strings**  
	List of models to fit on the data. If 'all', all available models are used. Use the predefined acronyms to select the models. Possible values are (case insensitive):    
		- 'GNB' for [Gaussian Naïve Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) (no hyperparameter tuning)
		- 'MNB' for [Multinomial Naïve Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)  
		- 'BNB' for [Bernoulli Naïve Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html)  
		- 'GP' for Gaussian Process [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html) (no hyperparameter tuning)
		- 'OLS' for [Ordinary Least Squares](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) (no hyperparameter tuning)
		- 'Ridge' for Ridge Linear [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
		- 'Lasso' for [Lasso Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html)
		- 'EN' for [ElasticNet Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html)
		- 'BR' for [Bayesian Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html) (with ridge regularization)
		- 'LR' for [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)  
		- 'LDA' for [Linear Discriminant Analysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html) 
		- 'QDA' for [Quadratic Discriminant Analysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html)
		- 'KNN' for K-Nearest Neighbors [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html)
		- 'Tree' for a single Decision Tree [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
		- 'Bag' for Bagging [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html) (with decision tree as base estimator)
		- 'ET' for Extra-Trees [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html)
		- 'RF' for Random Forest [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
		- 'AdaB' for AdaBoost [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html) (with decision tree as base estimator)
		- 'GBM' for Gradient Boosting Machine [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html) 
		- 'XGB' for XGBoost [classifier/regressor](https://xgboost.readthedocs.io/en/latest/python/python_api.html#module-xgboost.sklearn) (if package is available)  
		- 'LGB' for LightGBM [classifier](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMClassifier.html)/[regressor](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRegressor.html) (if package is available)
		- 'CatB' for CatBoost [classifier](https://catboost.ai/docs/concepts/python-reference_catboostclassifier.html)/[regressor](https://catboost.ai/docs/concepts/python-reference_catboostregressor.html) (if package is available)
		- 'lSVM' for Linear Support Vector Machine [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html) 
		- 'kSVM' for Kernel (non-linear) Support Vector Machine [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html)
		- 'PA' for Passive Aggressive [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html)
		- 'SGD' for Stochastic Gradient Descent [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html)
		- 'MLP' for Multilayer Perceptron [classifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)/[regressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor) 
	+ **metric: string or callable**  
	Metric on which the pipeline fits the models. Choose from any of the metrics described [here](https://github.com/tvdboom/ATOM#Metrics) or use a score (or loss) function with signature `metric(y, y_pred, **kwargs)`.
	+ **greater_is_better: bool, optional (default=True)**  
	Wether the metric is a score function or a loss function, i.e. if True, a higher score is better and if False, lower is better. Will be ignored if the metric is one of the pre-defined (string) metrics. 
	+ **needs_proba: bool, optional (default=False)**  
	Whether the metric function requires predict_proba to get probability estimates out of a classifier. Will be ignored if the metric is one of the pre-defined (string) metrics.
	+ **successive_halving: bool, optional (default=False)**  
	Fit the pipeline using a successive halving approach, that is, fitting the model on 1/N of the data, where N stands for the number of models still in the pipeline. After this, the best half of the models are selected for the next iteration. This process is repeated until only one model is left. Since models perform quite differently depending on the size of the training set, we recommend to use this feature when fitting similar models (e.g: only using tree-based models).
	+ **skip_iter: int, optional (default=0)**  
	Skip n last iterations of the successive halving.
	+ **max_iter: int, optional (default=15)**  
	Maximum number of iterations of the BO. 0 to not use the BO and fit the model directly on its default parameters.
	+ **max_time: int, optional (default=np.inf)**  
	Maximum time allowed for the BO (in seconds).
	+ **eps: float, optional (default=1e-08)**  
	Minimum hyperparameter distance between two consecutive steps in the BO.
	+ **batch_size: int, optional (default=1)**  
	Size of the batch in which the objective is evaluated.
	+ **init_points: int, optional (default=5)**  
	Initial number of tests the BO runs before fitting the surrogate function.
	+ **plot_bo: bool, optional (default=False)**  
	Wether to plot the BO's progress as it runs. Creates a canvas with two plots: the first plot shows the score of every trial and the second shows the distance between the last consecutive steps. Don't forget to call `%matplotlib` at the start of the cell if you are using jupyter notebook!
	+ **cv: bool, optional (default=3)**  
	Strategy to fit and score the model selected after every step of the BO.
		- if 1, randomly split the training data into a train and validation set
		- if >1, perform a k-fold cross validation on the training set
	+ **bagging: None or int, optional (default=None)**  
	Number of data sets (bootstrapped from the training set) to use in the bagging algorithm. If None, no bagging is performed.


Methods (utilities)
----------------------------- 
* **stats()**  
Print out a list of basic statistics on the dataset.<br><br>
* **report(df='dataset', rows=None, filename=None)**  
Get an extensive profile analysis of the data. The report is rendered in HTML5 and CSS3 and can be accessed through the `report` attribute. Note that this method can be very slow for large datasets. Dependency: [pandas-profiling](https://pandas-profiling.github.io/pandas-profiling/docs/).
	+ **df: string, optional (default='dataset')**  
	Name of the data class attribute to get the report from.
	+ **rows: None or int, optional (default=None)**  
	Number of rows selected randomly from the dataset to perform the analysis on. None to select all rows.
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved (as .html). None to not save anything.<br><br>
* **reset_attributes(truth='dataset')**  
If you change any of the class' data attributes (dataset, X, y, train, test, X_train, X_test, y_train, y_test) in between the pipeline, you should call this method to change all other data attributes to their correct values. Independent attributes are updated in unison, that is, setting truth='X_train' will also update X_test, y_train and y_test, or truth='train' will also update the test set, etc...
	+ **truth: string, optional (default='dataset')**  
	Data attribute that has been changed (as string)<br><br>
* **plot_bagging(iteration=-1, title=None, figsize=None, filename=None)**  
Make a boxplot of the bagging's results after fitting the class.
	+ **iteration: int, optional (default=-1)**  
	Iteration of the successive_halving to plot. If -1, use the last iteration.
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: None or 2d-tuple, optional (default=None)**  
	Figure size: format as (x, y). If None, adjusts to the number of models.
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_correlation(title=None, figsize=(10, 6), filename=None)**  
Make a correlation maxtrix plot of the dataset. Ignores non-numeric columns.
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: 2d-tuple, optional (default=(10, 6))**  
	Figure size: format as (x, y).
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_PCA(show=None, title=None, figsize=None, filename=None)**  
Plot the explained variance ratio of the components. Only if PCA was applied on the dataset through the feature_selection method.
	+ **show: int, optional (default=20)**  
	Number of best components to show in the plot. None for all components.  
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: 2d-tuple, optional (default=None)**  
	Figure size: format as (x, y). If None, adjust to the number of components shown.
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_successive_halving(title=None, figsize=(10, 6), filename=None)**  
Make a plot of the models' scores per iteration of the successive halving.
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: 2d-tuple, optional (default=(10, 6))**  
	Figure size: format as (x, y).
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_ROC(title=None, figsize=(10, 6), filename=None)**  
Plot the ROC curve of all the models. Only for binary classification tasks.  
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: 2d-tuple, optional (default=(10, 6))**  
	Figure size: format as (x, y).
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_PRC(title=None, figsize=(10, 6), filename=None)**  
Plot the precision-recall curve of all the models. Only for binary classification tasks.  
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: 2d-tuple, optional (default=(10, 6))**  
	Figure size: format as (x, y).
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **Additionnaly, you can call different metrics as methods of the main class to get the results of the fit method on this specific metric, e.g: `atom.precision()`. For a list of the available metrics click [here](https://github.com/tvdboom/ATOM#Metrics).**


Class attributes  
-----------------------------  
* **dataset**: Dataframe of the complete dataset.
* **X, y**: Data features and target.
* **train, test**: Train and test set.
* **X_train, y_train**: Training set features and target.
* **X_test, y_test**: Test set features and target.
* **mapping**: Dictionary of the target values mapped to their encoded integer (only for classification tasks).
* **report**: Pandas profiling report of the selected dataset (if the report method was used).
* **genetic_features**: Contains the description of the generated features and their scores (if feature_insertion was used).
* **collinear**: Dataframe of the collinear features and their correlation values (if feature_selection was used).
* **errors**: Dictionary of the encountered exceptions (if any) while fitting the models.
* **results**: Dataframe (or array of dataframes if successive_halving=True) of the results.


Class methods
-----------------------------
The plotting aesthetics can be changed using the following `@classmethods` (e.g. `ATOMClassifier.set_style('white')`):

* **set_style(style='darkgrid')**  
Change the seaborn plotting style.
	+ **style: string, optional (default='darkgrid')**  
	Name of the style to use. Possible values are: darkgrid, whitegrid, dark, white, and ticks.<br><br>
* **set_palette(palette='GnBu_d')**  
Change the seaborn color palette.
	+ **palette: string, optional (default='GnBu_d')**  
	Name of the palette to use. Click [here](https://seaborn.pydata.org/tutorial/color_palettes.html) for more information.<br><br>
* **set_title_fontsize(fontsize=20)**  
Change the fontsize of the plot's title.
	+ **fontsize: int, optional (default=20)**  
	Size of the font.<br><br>	
* **set_label_fontsize(fontsize=16)**  
Change the fontsize of the plot's labels and legends.
	+ **fontsize: int, optional (default=16)**  
	Size of the font.<br><br>	
* **set_tick_fontsize(fontsize=12)**  
Change the fontsize of the plot's ticks.
	+ **fontsize: int, optional (default=12)**  
	Size of the font.<br><br>	
	

### After fitting, the models become subclasses of the main class. They can be called upon for  handy plot functions and attributes. If successive_halving=True, the model subclass corresponds to the last fitted model.


Subclass methods  
-----------------------------  
* **plot_threshold(metric=None, steps=100, title=None, figsize=(10, 6), filename=None)**  
Plot performance metrics against multiple threshold values. If None, the metric used to fit the model will be selected. Only for binary classification tasks.  
	+ **metric: None, string, callable or list, optional (default=None)**  
	Metric(s) to plot. If None, the selected metric will be the one chosen to fit the model.
   	+ **steps: int, optional (default=100)**  
    	Number of thresholds (steps) to plot.
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: 2d-tuple, optional (default=(10, 6))**  
	Figure size: format as (x, y).
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_probabilities(target=1, title=None, figsize=(10, 6), filename=None)**  
Plot the probability of every class in the target variable against the class selected by target_class. Only for classification tasks.
	+ **target: int or string, optional (default=1)**  
	Target class to plot the probabilities against. Either the class' name or the index (0 corresponds to the first class, 1 to the second, etc...).
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: 2d-tuple, optional (default=(10, 6))**  
	Figure size: format as (x, y).
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_permutation_importance(show=20, n_repeats=10, title=None, figsize=None, filename=None)**  
Plot the feature importance permutation scores in a boxplot. A dictionary containing the permutation's results can be accessed through the `permutations` attribute.
	+ **n_repeats: int, optional (default=10)**  
	Number of times to permute a feature.
	+ **show: int, optional (default=20)**  
	Number of best features to show in the plot. None for all features.  
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: None or 2d-tuple, optional (default=None)**  
	Figure size: format as (x, y). If None, adjusts to the number of features shown.
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_feature_importance(show=None, title=None, figsize=None, filename=None)**  
Plot the normalized feature importance scores. Only works with tree based algorithms.
	+ **show: int, optional (default=None)**  
	Number of best features to show in the plot. None for all features.  
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: None or 2d-tuple, optional (default=None)**  
	Figure size: format as (x, y). If None, adjusts to the number of features shown.
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_ROC(title=None, figsize=(10, 6), filename=None)**  
Plot the ROC curve. Only for binary classification tasks.  
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: 2d-tuple, optional (default=(10, 6))**  
	Figure size: format as (x, y).
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_PRC(title=None, figsize=(10, 6), filename=None)**  
Plot the precision-recall curve. Only for binary classification tasks.  
	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: 2d-tuple, optional (default=(10, 6))**  
	Figure size: format as (x, y).
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **plot_confusion_matrix(normalize=True, title=None, figsize=(10, 6), filename=None)**  
Plot the confusion matrix for the model. Only for classification tasks.
	+ **normalize: bool, optional (default=True)**  
	Wether to normalize the confusion matrix.
 	+ **title: None or string, optional (default=None)**  
	Plot's title. None for default title.
	+ **figsize: 2d-tuple, optional (default=(10, 6))**  
	Figure size: format as (x, y).
	+ **filename: None or string, optional (default=None)**  
	Name of the file when saved. None to not save anything.<br><br>
* **save(filename=None)**  
Save the best found model as a pickle file.
	 + **filename: None or string, optional (default=None)**  
	Name of the file when saved. If None, it will be saved as 'ATOM_[model_type].pkl'.


Subclass attributes
-----------------------------  
* **error**: If the model encountered an exception, this shows it.
* **best_params**: Get parameters of the model with highest score.
* **best_model**: Get the model with highest score (not fitted).
* **best_model_fit**: Get the model with highest score fitted on the training set.
* **predict_train**: Get the predictions on the training set.
* **predict_test**: Get the predictions on the test set.
* **predict_proba_train**: Get the predicted probabilities on the training set.
* **predict_proba_test**: Get the predicted probabilities on the test set.
* **score_train**: Metric score of the BO's selected model on the training set.
* **score_test**: Metric score of the BO's selected model on the test set.
* **bagging_scores**: Array of the bagging's results.
* **permutations**: Dictionary of the permutation's results (if plot_permutation_importance was used).
* **BO**: Dictionary containing the information of every step taken by the BO.
	+ 'params': Parameters used for the model
	+ 'score': Score of the chosen metric
* **Any of the metrics described [here](https://github.com/tvdboom/ATOM#Metrics).**

Metrics
-----------------------------  
Some of the most common metrics are integrated in the ATOM class. They can be filled in the metric parameter of the fit method, called as method of the main class (e.g. `atom.rf.accuracy()`) and they are saved as attributes of every model subclass (e.g. `atom.rf.recall`). All metrics are calculated on the test set. For multiclass tasks, the type of averaging performed on the data is 'weighted'. The available metrics are:  
* For binary classification tasks only:  
	+ **tn** for the number of true negatives  
	+ **fp** for the number of false positives  
	+ **fn** for the number of false negatives  
	+ **tp** for the number of true positives  
	+ **ap** for the [average_precision_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html)	
* For classification tasks only:  
	+ **accuracy** for the [accuracy_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)
	+ **auc** for the [roc_auc_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html)
	+ **mcc** for the [matthews_corrcoef](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html)
	+ **f1** for the [f1_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)
	+ **hamming** for the [hamming_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html)
	+ **jaccard** for the [jaccard_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html)
	+ **logloss** for the [log_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html)
	+ **precision** for the [precision_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html)
	+ **recall** for the [recall_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html) 
* For all tasks:  
	+ **mae** for the [mean_absolute_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html)
	+ **max_error** for the [max_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html)
	+ **mse** for the [mean_squared_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)  
	+ **msle** for the [mean_squared_log_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html)  
	+ **r2** for the [r2_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)


Dependencies
-----------------------------
* **[numpy](https://numpy.org/)** (>=1.17.2)
* **[pandas](https://pandas.pydata.org/)** (>=0.25.1)
* **[scikit-learn](https://scikit-learn.org/stable/)** (>=0.22)
* **[tqdm](https://tqdm.github.io/)** (>=4.35.0)
* **[gpyopt](https://sheffieldml.github.io/GPyOpt/)** (>=1.2.5)
* **[matplotlib](https://matplotlib.org/)** (>=3.1.0)
* **[seaborn](https://seaborn.pydata.org/)** (>=0.9.0)
* **[imbalanced-learn](https://imbalanced-learn.readthedocs.io/en/stable/api.html)**, optional (>=0.5.0)
* **[pandas-profiling](https://pandas-profiling.github.io/pandas-profiling/docs/)**, optional (>=2.3.0)
* **[gplearn](https://gplearn.readthedocs.io/en/stable/index.html)**, optional (>=0.4.1)
* **[xgboost](https://xgboost.readthedocs.io/en/latest/)**, optional (>=0.90)
* **[lightgbm](https://lightgbm.readthedocs.io/en/latest/)**, optional (>=2.3.0)
* **[catboost](https://catboost.ai/docs/concepts/about.html)**, optional (>=0.19.1)
