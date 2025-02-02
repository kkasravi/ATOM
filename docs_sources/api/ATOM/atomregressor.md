# ATOMRegressor
----------------

<div style="font-size:20px">
<em>class</em> atom.api.<strong style="color:#008AB8">ATOMRegressor</strong>(*arrays,
y=-1, shuffle=True, n_rows=1, test_size=0.2, holdout_size=None, n_jobs=1,
verbose=0, warnings=True, logger=None, experiment=None, random_state=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/api.py#L312">[source]</a>
</span>
</div>

ATOMRegressor is ATOM's wrapper for regression tasks. Use this class to easily apply
all data transformations and model management provided by the package on a given
dataset. Note that contrary to sklearn's API, an ATOMRegressor instance already
contains the dataset on which we want to perform the analysis. Calling a method will
automatically apply it on the dataset it contains.

You can [predict](../../../user_guide/predicting), [plot](../../../user_guide/plots)
and call any [model](../../../user_guide/models) from atom. Read more in the
[user guide](../../../user_guide/first_steps).

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<strong>*arrays: sequence of indexables</strong><br>
Dataset containing features and target. Allowed formats are:
<ul style="line-height:1.2em;margin-top:5px">
<li>X</li>
<li>X, y</li>
<li>train, test</li>
<li>train, test, holdout</li>
<li>X_train, X_test, y_train, y_test</li>
<li>X_train, X_test, X_holdout, y_train, y_test, y_holdout</li>
<li>(X_train, y_train), (X_test, y_test)</li>
<li>(X_train, y_train), (X_test, y_test), (X_holdout, y_holdout)</li>
</ul>
X, train, test: dataframe-like<br>
<p style="margin-top:0;margin-left:15px">
Feature set with shape=(n_samples, n_features).</p>
y: int, str or sequence<br>
<ul style="line-height:1.2em;margin-top:5px">
<li>If int: Position of the target column in X.</li>
<li>If str: Name of the target column in X.</li>
<li>Else: Target column with shape=(n_samples,).</li>
</ul>
<strong>y: int, str or sequence, optional (default=-1)</strong><br>
<ul style="line-height:1.2em;margin-top:5px;margin-bottom:0">
<li>If int: Position of the target column in X.</li>
<li>If str: Name of the target column in X.</li>
<li>Else: Target column with shape=(n_samples,).</li>
</ul>
<p style="margin-top:5px">
This parameter is ignored if the target column is provided
through <code>arrays</code>.
</p>
<p>
<strong>shuffle: bool, optional (default=True)</strong><br>
Whether to shuffle the dataset before splitting the train and
test set. Be aware that not shuffling the dataset can cause
an unequal distribution of the target classes over the sets.
</p>
<strong>n_rows: int or float, optional (default=1)</strong><br>
Random subsample of the provided dataset to use. The default
value selects all the rows.
<ul style="line-height:1.2em;margin-top:5px">
<li>If <=1: Select this fraction of the dataset.</li>
<li>If >1: Select this exact number of rows. Only if the input
doesn't already specify the data sets (i.e. X or X, y).</li>
</ul>
<strong>test_size: int or float, optional (default=0.2)</strong><br>
<ul style="line-height:1.2em;margin-top:5px;margin-bottom:0">
<li>If <=1: Fraction of the dataset to include in the test set.</li>
<li>If >1: Number of rows to include in the test set.</li>
</ul>
<p style="margin-top:5px">
This parameter is ignored if the test set is provided through
<code>arrays</code>.</p>
<strong>holdout_size: int, float or None, optional (default=None)</strong><br>
<ul style="line-height:1.2em;margin-top:5px;margin-bottom:0">
<li>If None: No holdout data set is kept apart.</li>
<li>If <=1: Fraction of the dataset to include in the holdout set.</li>
<li>If >1: Number of rows to include in the holdout set.</li>
</ul>
<p style="margin-top:5px">
This parameter is ignored if the holdout set is provided through
<code>arrays</code>.</p>
<strong>n_jobs: int, optional (default=1)</strong><br>
Number of cores to use for parallel processing.
<ul style="line-height:1.2em;margin-top:5px;margin-bottom:0">
<li>If >0: Number of cores to use.</li>
<li>If -1: Use all available cores.</li>
<li>If <-1: Use available_cores - 1 + <code>n_jobs</code>.</li>
</ul>
<p style="margin-top:5px">
Beware that using multiple processes on the same machine may cause
memory issues for large datasets.</p>
<strong>verbose: int, optional (default=0)</strong><br>
Verbosity level of the class. Possible values are:
<ul style="line-height:1.2em;margin-top:5px">
<li>0 to not print anything.</li>
<li>1 to print basic information.</li>
<li>2 to print detailed information.</li>
</ul>
<strong>warnings: bool or str, optional (default=True)</strong><br>
<ul style="line-height:1.2em;margin-top:5px;margin-bottom:0">
<li>If True: Default warning action (equal to "default").</li>
<li>If False: Suppress all warnings (equal to "ignore").</li>
<li>If str: One of the actions in python's warnings environment.</li>
</ul>
<p style="margin-top:5px">
Changing this parameter affects the <code>PYTHONWARNINGS</code> environment.
<br>ATOM can't manage warnings that go directly from C/C++ code to stdout.</p>
<strong>logger: str, Logger or None, optional (default=None)</strong><br>
<ul style="line-height:1.2em;margin-top:5px">
<li>If None: Doesn't save a logging file.</li>
<li>If str: Name of the log file. Use "auto" for automatic naming.</li>
<li>Else: Python <code>logging.Logger</code> instance.</li>
</ul>
<p>
<strong>experiment: str or None, optional (default=None)</strong><br>
Name of the mlflow experiment to use for tracking. If None,
no mlflow tracking is performed.
</p>
<p>
<strong>random_state: int or None, optional (default=None)</strong><br>
Seed used by the random number generator. If None, the random number
generator is the <code>RandomState</code> instance used by <code>np.random</code>.
</p>
</td>
</tr>
</table>
<br>



## Magic methods

The class contains some magic methods to help you access some of its
elements faster. Note that methods that apply on the pipeline can return
different results per branch.

* **\__repr__:** Prints an overview of atom's branches, models, metric and errors.
* **\__len__:** Returns the length of the dataset.
* **\__iter__:** Iterate over the pipeline's transformers.
* **\__contains__:** Checks if the provided item is a column in the dataset.
* **\__getitem__:** If int, return the i-th transformer in the pipeline.
  If str, access a branch, a model, a column or a subset of the dataset.

<br>



## Attributes

### Data attributes

The dataset can be accessed at any time through multiple attributes,
e.g. calling `atom.train` will return the training set. Updating one
of the data attributes will automatically update the rest as well.
Changing the branch will also change the response from these attributes
accordingly.

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Attributes:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>pipeline: pd.Series</strong><br>
Series containing all transformers fitted on the data in the current branch.
Use this attribute only to access the individual instances. To visualize the
pipeline, use the status method from the branch or the
<a href="../../plots/plot_pipeline">plot_pipeline</a> method.
</p>
<p>
<strong>feature_importance: list</strong><br>
Features ordered by most to least important. This attribute is created
after running the <a href="#feature-selection">feature_selection</a>,
<a href="../../plots/plot_permutation_importance">plot_permutation_importance</a>
or <a href="../../plots/plot_feature_importance">plot_feature_importance</a> methods.
</p>
<p>
<strong>dataset: pd.DataFrame</strong><br>
Complete dataset in the pipeline.
</p>
<p>
<strong>train: pd.DataFrame</strong><br>
Training set.
</p>
<p>
<strong>test: pd.DataFrame</strong><br>
Test set.
</p>
<p>
<strong>X: pd.DataFrame</strong><br>
Feature set.
</p>
<p>
<strong>y: pd.Series</strong><br>
Target column.
</p>
<p>
<strong>X_train: pd.DataFrame</strong><br>
Training features.
</p>
<p>
<strong>y_train: pd.Series</strong><br>
Training target.
</p>
<p>
<strong>X_test: pd.DataFrame</strong><br>
Test features.
</p>
<p>
<strong>y_test: pd.Series</strong><br>
Test target.
</p>
<p>
<strong>shape: tuple</strong><br>
Dataset's shape: (n_rows x n_columns) or (n_rows, (shape_sample), n_cols)
for datasets with more than two dimensions.
</p>
<p>
<strong>columns: list</strong><br>
Names of the columns in the dataset.
</p>
<p>
<strong>n_columns: int</strong><br>
Number of columns in the dataset.
</p>
<p>
<strong>features: list</strong><br>
Names of the features in the dataset.
</p>
<p>
<strong>n_features: int</strong><br>
Number of features in the dataset.
</p>
<p>
<strong>target: str</strong><br>
Name of the target column.
</p>
<p>
<strong>scaled: bool</strong><br>
Whether the feature set is scaled. It is considered scaled when
it has mean=0 and std=1, or when atom has a scaler in the pipeline.
</p>
<p>
<strong>duplicates: int</strong><br>
Number of duplicate rows in the dataset.
</p>
<p>
<strong>nans: pd.Series</strong><br>
Columns with the number of missing values in them.
</p>
<p>
<strong>n_nans: int</strong><br>
Number of samples containing missing values.
</p>
<p>
<strong>numerical: list</strong><br>
Names of the numerical features in the dataset.
</p>
<p>
<strong>n_numerical: int</strong><br>
Number of numerical features in the dataset.
</p>
<p>
<strong>categorical: list</strong><br>
Names of the categorical features in the dataset.
</p>
<p>
<strong>n_categorical: int</strong><br>
Number of categorical features in the dataset.
</p>
<p>
<strong>outliers: pd.Series</strong><br>
Columns in training set with amount of outlier values.
</p>
<p>
<strong>n_outliers: int</strong><br>
Number of samples in the training set containing outliers.
</p>
</td>
</tr>
</table>
<br>


### Utility attributes

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Attributes:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>missing: list</strong><br>
List of values that are considered "missing" (used by the <a href="#clean">clean</a>
and <a href="#impute">impute</a> methods). Default values are: "", "?", "None", "NA",
"nan", "NaN" and "inf". Note that <code>None</code>, <code>NaN</code>, <code>+inf</code>
and <code>-inf</code> are always considered missing since they are incompatible with
sklearn estimators.
</p>
<p>
<strong>models: list</strong><br>
List of models in the pipeline.
</p>
<p>
<strong>metric: str or list</strong><br>
Metric(s) used to fit the models.
</p>
<p>
<strong>errors: dict</strong><br>
Dictionary of the encountered exceptions (if any).
</p>
<p>
<strong>winner: <a href="../../../user_guide/models">model</a></strong><br>
Model subclass that performed best on the test set (either through the
<code>metric_test</code> or <code>mean_bootstrap</code> attribute).
</p>
<strong>results: pd.DataFrame</strong><br>
Dataframe of the training results. Columns can include:
<ul style="line-height:1.2em;margin-top:5px">
<li><b>metric_bo:</b> Best score achieved during the BO.</li>
<li><b>time_bo:</b> Time spent on the BO.</li>
<li><b>metric_train:</b> Metric score on the training set.</li>
<li><b>metric_test:</b> Metric score on the test set.</li>
<li><b>time_fit:</b> Time spent fitting and evaluating.</li>
<li><b>mean_bootstrap:</b> Mean score of the bootstrap results.</li>
<li><b>std_bootstrap:</b> Standard deviation score of the bootstrap results.</li>
<li><b>time_bootstrap:</b> Time spent on the bootstrap algorithm.</li>
<li><b>time:</b> Total time spent on the whole run.</li>
</ul>
</td>
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Additional:</strong></td>
<td width="80%" class="td_params">
<strong>Attributes and methods for dataset</strong><br>
Some attributes and methods can be called from atom but will return
the call from the dataset in the current branch, e.g. <code>atom.dtypes</code>
shows the types of every column in the dataset. These attributes and
methods are: "size", "head", "tail", "loc", "iloc", "describe", "iterrows",
"dtypes", "at", "iat".
</td>
</tr>
</table>
<br>


### Plot attributes
 
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Attributes:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>style: str</strong><br>
Plotting style. See seaborn's <a href="https://seaborn.pydata.org/tutorial/aesthetics.html#seaborn-figure-styles">documentation</a>.
</p>
<p>
<strong>palette: str</strong><br>
Color palette. See seaborn's <a href="https://seaborn.pydata.org/tutorial/color_palettes.html">documentation</a>.
</p>
<p>
<strong>title_fontsize: int</strong><br>
Fontsize for the plot's title.
</p>
<p>
<strong>label_fontsize: int</strong><br>
Fontsize for labels and legends.
</p>
<p>
<strong>tick_fontsize: int</strong><br>
Fontsize for the ticks along the plot's axes.
</p>
</td>
</tr>
</table>
<br><br>



## Utility methods

The class contains a variety of utility methods to handle the data and
manage the pipeline.

<table style="font-size:16px;margin-top:5px">
<tr>
<td><a href="#add">add</a></td>
<td>Add a transformer to the current branch.</td>
</tr>

<tr>
<td><a href="#apply">apply</a></td>
<td>Apply a function to the dataset.</td>
</tr>

<tr>
<td><a href="#automl">automl</a></td>
<td>Search for an optimized pipeline in an automated fashion.</td>
</tr>

<tr>
<td><a href="#available-models">available_models</a></td>
<td>Give an overview of the available predefined models.</td>
</tr>

<tr>
<td><a href="#canvas">canvas</a></td>
<td>Create a figure with multiple plots.</td>
</tr>

<tr>
<td><a href="#clear">clear</a></td>
<td>Clear attributes from all models.</td>
</tr>

<tr>
<td><a href="#delete">delete</a></td>
<td>Delete models from the trainer.</td>
</tr>

<tr>
<td><a href="#distribution">distribution</a></td>
<td>Get statistics on a column's distribution.</td>
</tr>

<tr>
<td><a href="#drop">drop</a></td>
<td>Drop columns from the dataset.</td>
</tr>

<tr>
<td><a href="#evaluate">evaluate</a></td>
<td>Get all models' scores for the provided metrics.</td>
</tr>

<tr>
<td><a href="#export-pipeline">export_pipeline</a></td>
<td>Export the pipeline to a sklearn-like Pipeline object.</td>
</tr>

<tr>
<td><a href="#log">log</a></td>
<td>Save information to the logger and print to stdout.</td>
</tr>

<tr>
<td><a href="#merge">merge</a></td>
<td>Merge another trainer into this one.</td>
</tr>

<tr>
<td><a href="#report">report</a></td>
<td>Get an extensive profile analysis of the data.</td>
</tr>

<tr>
<td><a href="#reset">reset</a></td>
<td>Reset the instance to it's initial state.</td>
</tr>

<tr>
<td><a href="#reset-aesthetics">reset_aesthetics</a></td>
<td>Reset the plot aesthetics to their default values.</td>
</tr>

<tr>
<td><a href="#save">save</a></td>
<td>Save the instance to a pickle file.</td>
</tr>

<tr>
<td><a href="#save-data">save_data</a></td>
<td>Save data to a csv file.</td>
</tr>

<tr>
<td><a href="#shrink">shrink</a></td>
<td>Converts the dataset's columns to the smallest possible dtype.</td>
</tr>

<tr>
<td><a href="#stacking">stacking</a></td>
<td>Add a Stacking instance to the models in the pipeline.</td>
</tr>

<tr>
<td><a href="#stats">stats</a></td>
<td>Print out a list of basic statistics on the dataset.</td>
</tr>

<tr>
<td><a href="#status">status</a></td>
<td>Get an overview of atom's branches, models and errors.</td>
</tr>

<tr>
<td><a href="#voting">voting</a></td>
<td>Add a Voting instance to the models in the pipeline.</td>
</tr>
</table>
<br>


<a name="add"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">add</strong>(transformer,
columns=None, train_only=False, **fit_params)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L828">[source]</a>
</span>
</div>
Add a transformer to the current branch. If the transformer is
not fitted, it is fitted on the complete training set. Afterwards,
the data set is transformed and the transformer is added to atom's
pipeline. If the transformer is a sklearn Pipeline, every transformer
is merged independently with atom.

!!! warning

    * The transformer should have fit and/or transform methods with arguments
      `X` (accepting an array-like object of shape=(n_samples, n_features))
      and/or `y` (accepting a sequence of shape=(n_samples,)).
    * The transform method should return a feature set as an array-like
      object of shape=(n_samples, n_features) and/or a target column as a
      sequence of shape=(n_samples,).

!!! note
    If the transform method doesn't return a dataframe:

    * The column naming happens as follows. If the transformer returns the
      same number of columns, the names are kept equal. If the number of
      columns change, old columns will keep their name (as long as the column
      is unchanged) and new columns will receive the name `Feature n`, where
      n stands for the n-th feature. This means that a transformer should
      only transform, add or drop columns, not combinations of these.
    * The index remains the same as before the transformation. This means
      that the transformer should not add, remove or shuffle rows unless it
      returns a dataframe.

!!! note
    If the transformer has a `n_jobs` and/or `random_state` parameter that
    is left to its default value, it adopts atom's value.

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>transformer: estimator</strong><br>
Transformer to add to the pipeline. Should implement a <code>transform</code> method.
</p>
<p>
<strong>columns: int, str, slice, sequence or None, optional (default=None)</strong><br>
Names, indices or dtypes of the columns in the dataset to transform.
If None, transform all columns. Add <code>!</code> in front of a name
or dtype to exclude that column, e.g. <code>atom.add(Transformer(), columns="!Location")</code>
transforms all columns except <code>Location</code>. You can either
include or exclude columns, not combinations of these.
</p>
<p>
<strong>train_only: bool, optional (default=False)</strong><br>
Whether to apply the estimator only on the training set or
on the complete dataset. Note that if True, the transformation
is skipped when making predictions on unseen data.
</p>
<p>
<strong>**fit_params</strong><br>
Additional keyword arguments for the fit method of the transformer.
</p>
</td>
</tr>
</table>
<br />


<a name="apply"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">apply</strong>(func,
columns, args=(), **kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L875">[source]</a>
</span>
</div>
Transform one column in the dataset using a function (can
be a lambda). If the provided column is present in the dataset,
that same column is transformed. If it's not a column in the
dataset, a new column with that name is created. The first
parameter of the function is the complete dataset.

!!! note
    This approach is preferred over changing the dataset directly
    through the property's `@setter` since the transformation
    is saved to atom's pipeline.

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>func: callable</strong><br>
Function to apply to the dataset.
</p>
<p>
<strong>columns: int or str</strong><br>
Name or index of the column in the dataset to create or transform.
</p>
<p>
<strong>args: tuple, optional (default=())</strong><br>
Positional arguments for the function (after the dataset).
</p>
<p>
<strong>**kwargs</strong><br>
Additional keyword arguments for the function.
</p>
</td>
</tr>
</table>
<br />


<a name="automl"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">automl</strong>(**kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L296">[source]</a>
</span>
</div>
Uses the [TPOT](http://epistasislab.github.io/tpot/) package to perform
an automated search of transformers and a final estimator that maximizes
a metric on the dataset. The resulting transformations and estimator are
merged with atom's pipeline. The tpot instance can be accessed through the
`tpot` attribute. Read more in the [user guide](../../../user_guide/data_management/#automl).
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<strong>**kwargs</strong><br>
Keyword arguments for <a href="https://epistasislab.github.io/tpot/api/#regression">TPOTRegressor</a>.
</td>
</tr>
</table>
<br />


<a name="available-models"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">available_models</strong>()
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/basepredictor.py#L486">[source]</a>
</span>
</div>
Give an overview of the available predefined models.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>overview: pd.DataFrame</strong><br>
Information about the predefined models available for the current task.
Columns include:
<ul style="line-height:1.2em;margin-top:5px">
<li><b>acronym:</b> Model's acronym (used to call the model).</li>
<li><b>fullname:</b> Complete name of the model.</li>
<li><b>estimator:</b> The model's underlying estimator.</li>
<li><b>module:</b> The estimator's module.</li>
<li><b>needs_scaling:</b> Whether the model requires feature scaling.</li>
</ul>
</td>
</tr>
</table>
<br />


<a name="canvas"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">canvas</strong>(nrows=1,
ncols=2, title=None, figsize=None, filename=None, display=True)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/plots.py#L438">[source]</a>
</span>
</div>
This `@contextmanager` allows you to draw many plots in one figure.
The default option is to add two plots side by side. See the
[user guide](../../../user_guide/plots/#canvas) for an example.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>nrows: int, optional (default=1)</strong><br>
Number of plots in length.
</p>
<p>
<strong>ncols: int, optional (default=2)</strong><br>
Number of plots in width.
</p>
<p>
<strong>title: str or None, optional (default=None)</strong><br>
Plot's title. If None, no title is displayed.
</p>
<p>
<strong>figsize: tuple or None, optional (default=None)</strong><br>
Figure's size, format as (x, y). If None, it adapts the size to the
number of plots in the canvas.
</p>
<p>
<strong>filename: str or None, optional (default=None)</strong><br>
Name of the file. Use "auto" for automatic naming.
If None, the figure is not saved.
</p>
<p>
<strong>display: bool, optional (default=True)</strong><br>
Whether to render the plot.
</p>
</td>
</tr>
</table>
<br />


<a name="clear"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">clear</strong>()
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/basepredictor.py#L520">[source]</a>
</span>
</div>
Reset all model attributes to their initial state, deleting potentially
large data arrays. Use this method to free some memory before saving
the class. The cleared attributes per model are:

* [Prediction attributes](../../../user_guide/predicting).
* [Metrics scores](../../../user_guide/training/#metric).
* [Shap values](../../../user_guide/plots/#shap).

<br /><br /><br />


<a name="delete"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">delete</strong>(models=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/basepredictor.py#L535">[source]</a>
</span>
</div>
Delete models from the trainer. If all models are removed, the metric
is reset. Use this method to drop unwanted models from the pipeline
or to free some memory before saving. Deleted models are not removed
from any active mlflow experiment.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<strong>models: str or sequence, optional (default=None)</strong><br>
Models to delete. If None, delete them all.
</td>
</tr>
</table>
<br />


<a name="distribution"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">distribution</strong>(columns=0)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L366">[source]</a>
</span>
</div>
Compute the [KS-statistic](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)
for various distributions against a column in the dataset. Missing values are ignored.

!!! tip
    Use the [plot_distribution](../../plots/plot_distribution) method to plot
    the column's distribution.

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<strong>columns: int or str, optional (default=0)</strong><br>
Index or name of the column to get the statistics from. Only
numerical columns are accepted.
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>stats: pd.DataFrame</strong><br>
Dataframe with the statistic results.
</td>
</tr>
</table>
<br />


<a name="drop"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">drop</strong>(columns)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L918">[source]</a>
</span>
</div>
Drop columns from the dataset.

!!! note
    This approach is preferred over dropping columns from the
    dataset directly through the property's `@setter` since
    the transformation is saved to atom's pipeline.

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<strong>columns: int, str, slice or sequence</strong><br>
Names or indices of the columns to drop.
</td>
</tr>
</table>
<br />


<a name="evaluate"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">evaluate</strong>(metric=None,
dataset="test")
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/basepredictor.py#L562">[source]</a>
</span>
</div>
Get all the models' scores for the provided metrics.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>metric: str, func, scorer, sequence or None, optional (default=None)</strong><br>
Metrics to calculate. If None, a selection of the most common
metrics per task are used.
</p>
<p>
<strong>dataset: str, optional (default="test")</strong><br>
Data set on which to calculate the metric. Choose from: "train",
"test" or "holdout".
</p>
</td>
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>scores: pd.DataFrame</strong><br>
Scores of the models.
</td>
</tr>
</table>
<br />


<a name="export-pipeline"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">export_pipeline</strong>(model=None,
memory=None, verbose=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L408">[source]</a>
</span>
</div>
Export atom's pipeline to a sklearn-like Pipeline object. Optionally, you
can add a model as final estimator. The returned pipeline is already fitted
on the training set.

!!! info
    ATOM's Pipeline class behaves the same as a sklearn <a href="https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html">Pipeline</a>,
    and additionally:
    <ul style="line-height:1.2em;margin-top:5px">
    <li>Accepts transformers that change the target column.</li>
    <li>Accepts transformers that drop rows.</li>
    <li>Accepts transformers that only are fitted on a subset of the
        provided dataset.</li>
    <li>Always outputs pandas objects.</li>
    <li>Uses transformers that are only applied on the training set (see the
        <a href="#balance">balance</a> or <a href="#prune">prune</a> methods)
        to fit the pipeline, not to make predictions on unseen data.</li>
    </ul>

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>model: str or None, optional (default=None)</strong><br>
Name of the model to add as a final estimator to the pipeline. If the
model used <a href="../../../user_guide/training/#automated-feature-scaling">automated feature scaling</a>,
the <code>scaler</code> is added to the pipeline. If None, only the
transformers are added.
</p>
<strong>memory: bool, str, Memory or None, optional (default=None)</strong><br>
Used to cache the fitted transformers of the pipeline.
<ul style="line-height:1.2em;margin-top:5px">
<li>If None or False: No caching is performed.</li>
<li>If True: A default temp directory is used.</li>
<li>If str: Path to the caching directory.</li>
<li>If Memory: Object with the <a href="https://joblib.readthedocs.io/en/latest/generated/joblib.Memory.html">joblib.Memory</a> interface.</li>
</ul>
<p>
<strong>verbose: int or None, optional (default=None)</strong><br>
Verbosity level of the transformers in the pipeline. If None, it leaves
them to their original verbosity. Note that this is not the pipeline's
own verbose parameter. To change that, use the <code>set_params</code>
method.
</p>
</td>
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>pipeline: Pipeline</strong><br>
Current branch as a sklearn-like Pipeline object.
</td>
</tr>
</table>
<br />


<a name="log"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">log</strong>(msg, level=0)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/basetransformer.py#L484">[source]</a>
</span>
</div>
Write a message to the logger and print it to stdout.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>msg: str</strong><br>
Message to write to the logger and print to stdout.
</p>
<p>
<strong>level: int, optional (default=0)</strong><br>
Minimum verbosity level to print the message.
</p>
</td>
</tr>
</table>
<br />


<a name="merge"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">merge</strong>(other, suffix="2")
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/basepredictor.py#L637">[source]</a>
</span>
</div>
Merge another trainer into this one. Branches, models, metrics and
attributes of the other trainer are merged into this one. If there
are branches and/or models with the same name, they are merged
adding the `suffix` parameter to their name. The errors and missing
attributes are extended with those of the other instance. It's only
possible to merge two instances if they are initialized with the same
dataset and trained with the same metric.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>other: trainer</strong><br>
Trainer instance with which to merge.
</p>
<p>
<strong>suffix: str, optional (default="2")</strong><br>
Conflicting branches and models are merged adding <code>suffix</code>
to the end of their names.
</p>
</td>
</tr>
</table>
<br />


<a name="report"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">report</strong>(dataset="dataset",
n_rows=None, filename=None, **kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L482">[source]</a>
</span>
</div>
Create an extensive profile analysis report of the data. The report
is rendered in HTML5 and CSS3. Note that this method can be slow for
`n_rows` > 10k.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>dataset: str, optional (default="dataset")</strong><br>
Data set to get the report from.
</p>
<p>
<strong>n_rows: int or None, optional (default=None)</strong><br>
Number of (randomly picked) rows to process. None to use all rows.
</p>
<p>
<strong>filename: str or None, optional (default=None)</strong><br>
Name to save the file with (as .html). None to not save anything.
</p>
<p>
<strong>**kwargs</strong><br>
Additional keyword arguments for the ProfileReport instance.
</p>
</td>
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>report: <a href="https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/pages/api/_autosummary/pandas_profiling.profile_report.ProfileReport.html#pandas_profiling.profile_report.ProfileReport">ProfileReport</a></strong><br>
Created profile object.
</td>
</tr>
</table>
<br />


<a name="reset"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">reset</strong>()
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L532">[source]</a>
</span>
</div>
Reset the instance to it's initial state, i.e. it deletes all branches
and models. The dataset is also reset to its form after initialization.
<br /><br /><br />


<a name="reset-aesthetics"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">reset_aesthetics</strong>()
<span style="float:right"><a href="https://github.com/tvdboom/ATOM/blob/master/atom/plots.py#L221">[source]</a>
</span>
</div>
Reset the [plot aesthetics](../../../user_guide/plots/#aesthetics) to their default values.
<br /><br /><br />


<a name="save"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">save</strong>(filename="auto", save_data=True)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/basetransformer.py#L505">[source]</a>
</span>
</div>
Save the instance to a pickle file. Remember that the class contains
the complete dataset as attribute, so the file can become large for
big datasets! To avoid this, use `save_data=False`.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>filename: str, optional (default="auto")</strong><br>
Name of the file. Use "auto" for automatic naming.
</p>
<p>
<strong>save_data: bool, optional (default=True)</strong><br>
Whether to save the data as an attribute of the instance. If False,
remember to add the data to <a href="../../ATOM/atomloader">ATOMLoader</a>
when loading the file.
</p>
</td>
</tr>
</table>
<br>


<a name="save-data"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">save_data</strong>(filename="auto", dataset="dataset")
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L551">[source]</a>
</span>
</div>
Save the data in the current branch to a csv file.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>filename: str, optional (default="auto")</strong><br>
Name of the file. Use "auto" for automatic naming.
</p>
<p>
<strong>dataset: str, optional (default="dataset")</strong><br>
Data set to save.
</p>
</td>
</tr>
</table>
<br>


<a name="shrink"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">shrink</strong>(columns=None, obj2cat=True, int2uint=False)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L572">[source]</a>
</span>
</div>
Converts the dataset's columns to the smallest possible dtype.
Use this method for memory optimization. Note that applying
transformers to the data may alter the dtypes again.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>columns: int, str, slice, sequence or None, optional (default=None)</strong><br>
Names, indices or dtypes of the columns in the dataset to shrink.
If None, transform all columns.
</p>
<p>
<strong>obj2cat: bool, optional (default=True)</strong><br>
Whether to convert <code>object</code> to <code>category</code>. Only if the
number of categories would be less than 30% of the length
of the column.
</p>
<p>
<strong>int2uint: bool, optional (default=False)</strong><br>
Whether to convert <code>int</code> to <code>uint</code>. Only if the values are
strictly positive.
</p>
</td>
</tr>
</table>
<br />


<a name="stacking"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">stacking</strong>(name="Stack",
models=None, **kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/basepredictor.py#L705">[source]</a>
</span>
</div>
Add a [Stacking](../../../user_guide/models/#stacking) model to the pipeline.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>name: str, optional (default="Stack")</strong><br>
Name of the model. The name is always presided with the
model's acronym: <code>Stack</code>.
</p>
<p>
<strong>models: sequence or None, optional (default=None)</strong><br>
Models that feed the stacking estimator. If None, it selects
all non-ensemble models trained on the current branch.
</p>
<p>
<strong>**kwargs</strong><br>
Additional keyword arguments for sklearn's <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html">StackingRegressor</a>
instance. The <a href="../../../user_guide/models/#predefined-models">predefined model's</a>
acronyms can be used for the <code>final_estimator</code> parameter.
</td>
</tr>
</table>
<br />


<a name="stats"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">stats</strong>()
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L648">[source]</a>
</span>
</div>
Print basic information about the dataset.
<br /><br /><br />


<a name="status"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">status</strong>()
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L701">[source]</a>
</span>
</div>
Get an overview of the branches, models and errors in the instance.
This method prints the same information as atom's \__repr__ and also
saves it to the logger.
<br /><br /><br />


<a name="voting"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">voting</strong>(name="Vote",
models=None, **kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/basepredictor.py#L765">[source]</a>
</span>
</div>
Add a [Voting](../../../user_guide/models/#voting) model to the pipeline.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>name: str, optional (default="Vote")</strong><br>
Name of the model. The name is always presided with the
model's acronym: <code>Vote</code>.
</p>
<p>
<strong>models: sequence or None, optional (default=None)</strong><br>
Models that feed the voting estimator. If None, it selects
all non-ensemble models trained on the current branch.
</p>
<p>
<strong>**kwargs</strong><br>
Additional keyword arguments for sklearn's <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html">VotingRegressor</a>
instance.
</td>
</tr>
</table>
<br /><br />



## Data cleaning

The class provides data cleaning methods to scale or transform the
features and handle missing values, categorical columns and outliers.
Calling on one of them will automatically apply the method on the dataset
in the pipeline.

!!! tip
    Use the [report](#report) method to examine the data and help you
    determine suitable parameters for the data cleaning methods.
    

<table style="font-size:16px;margin-top:5px">
<tr>
<td><a href="#scale">scale</a></td>
<td>Scale the dataset.</td>
</tr>

<tr>
<td><a href="#gauss">gauss</a></td>
<td>Transform the data to follow a Gaussian distribution.</td>
</tr>

<tr>
<td><a href="#clean">clean</a></td>
<td>Applies standard data cleaning steps on the dataset.</td>
</tr>

<tr>
<td><a href="#impute">impute</a></td>
<td>Handle missing values in the dataset.</td>
</tr>

<tr>
<td><a href="#encode">encode</a></td>
<td>Encode categorical features.</td>
</tr>

<tr>
<td><a href="#prune">prune</a></td>
<td>Prune outliers from the training set.</td>
</tr>
</table>
<br>


<a name="scale"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">scale</strong>(strategy="standard", **kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L940">[source]</a>
</span>
</div>
Applies one of sklearn's scalers. Non-numerical columns are ignored. The
estimator created by the class is attached to atom. See the
[Scaler](../data_cleaning/scaler.md) class for a description of the parameters.
<br /><br /><br />


<a name="gauss"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">gauss</strong>(strategy="yeo-johnson", **kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L960">[source]</a>
</span>
</div>
Transform the data to follow a Gaussian distribution. This transformation
is useful for modeling issues related to heteroscedasticity (non-constant
variance), or other situations where normality is desired. Missing values
are disregarded in fit and maintained in transform. Categorical columns
are ignored. The estimator created by the class is attached to atom. See
the See the [Gauss](../data_cleaning/gauss.md) class for a description of
the parameters.
<br /><br /><br />


<a name="clean"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">clean</strong>(drop_types=None,
strip_categorical=True, drop_max_cardinality=True, drop_min_cardinality=True,
drop_duplicates=False, drop_missing_target=True, encode_target=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L986">[source]</a>
</span>
</div>
Applies standard data cleaning steps on the dataset. Use the parameters
to choose which transformations to perform. The available steps are:

* Drop columns with specific data types.
* Strip categorical features from white spaces.
* Drop categorical columns with maximal cardinality.
* Drop columns with minimum cardinality.
* Drop duplicate rows.
* Drop rows with missing values in the target column.
* Encode the target column (only for classification tasks).

See the [Cleaner](../data_cleaning/cleaner.md) class for a description of the parameters.
<br /><br /><br />


<a name="impute"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">impute</strong>(strat_num="drop",
strat_cat="drop", max_nan_rows=None, max_nan_cols=None, missing=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L1035">[source]</a>
</span>
</div>
Impute or remove missing values according to the selected strategy.
Also removes rows and columns with too many missing values. The
imputer is fitted only on the training set to avoid data leakage.
Use the `missing` attribute to customize what are considered "missing
values". See [Imputer](../data_cleaning/imputer.md) for a description
of the parameters. Note that since the Imputer can remove rows from
both the train and test set, the size of the sets may change after
the transformation.
<br /><br /><br />


<a name="encode"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">encode</strong>(strategy="LeaveOneOut",
max_onehot=10, ordinal=None, frac_to_other=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L1069">[source]</a>
</span>
</div>
Perform encoding of categorical features. The encoding type depends
on the number of unique values in the column:
<ul style="line-height:1.2em;margin-top:5px">
<li>If n_unique=2 or ordinal feature, use Label-encoding.</li>
<li>If 2 < n_unique <= max_onehot, use OneHot-encoding.</li>
<li>If n_unique > max_onehot, use `strategy`-encoding.</li>
</ul>
Missing values are propagated to the output column. Unknown classes
encountered during transforming are converted to `np.NaN`. The class
is also capable of replacing classes with low occurrences with the
value `other` in order to prevent too high cardinality. See
[Encoder](../data_cleaning/encoder.md) for a description of the parameters.

!!! note
    This method only encodes the categorical features. It does not encode
    the target column! Use the [clean](#clean) method for that.

<br /><br /><br />


<a name="prune"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">prune</strong>(strategy="z-score",
method="drop", max_sigma=3, include_target=False, **kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L1108">[source]</a>
</span>
</div>
Prune outliers from the training set. The definition of outlier depends
on the selected strategy and can greatly differ from one each other. 
Ignores categorical columns. The estimators created by the class
are attached to atom. See [Pruner](../data_cleaning/pruner.md) for a
description of the parameters.

!!! note
    This transformation is only applied to the training set in order
    to maintain the original distribution of samples in the test set.

<br /><br /><br />



## NLP

The Natural Language Processing (NLP) transformers help to convert raw
text to meaningful numeric values, ready to be ingested by a model.

<table style="font-size:16px;margin-top:5px">
<tr>
<td><a href="#textclean">textclean</a></td>
<td>Applies standard text cleaning to the corpus.</td>
</tr>

<tr>
<td><a href="#tokenize">tokenize</a></td>
<td>Convert documents into sequences of words</td>
</tr>

<tr>
<td><a href="#normalize">normalize</a></td>
<td>Convert words to a more uniform standard.</td>
</tr>

<tr>
<td><a href="#vectorize">vectorize</a></td>
<td>Transform the corpus into meaningful vectors of numbers.</td>
</tr>
</table>
<br>


<a name="textclean"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">textclean</strong>(decode=True,
lower_case=True, drop_emails=True, regex_emails=None, drop_url=True,
regex_url=None, drop_html=True, regex_html=None, drop_emojis, regex_emojis=None,
drop_numbers=True, regex_numbers=None, drop_punctuation=True)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/nlp.py#L1183">[source]</a>
</span>
</div>
Applies standard text cleaning to the corpus. Transformations include
normalizing characters and dropping noise from the text (emails, HTML
tags, URLs, etc...). The transformations are applied on the column
named `Corpus`, in the same order the parameters are presented. If
there is no column with that name, an exception is raised. See the
[TextCleaner](../nlp/textcleaner.md) class for a description of the
parameters.
<br /><br /><br />


<a name="tokenize"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">tokenize</strong>(bigram_freq=None,
trigram_freq=None, quadgram_freq=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/nlp.py#L1235">[source]</a>
</span>
</div>
Convert documents into sequences of words. Additionally, create
n-grams (represented by words united with underscores, e.g.
"New_York") based on their frequency in the corpus. The
transformations are applied on the column named `Corpus`. If
there is no column with that name, an exception is raised. See
the [Tokenizer](../nlp/tokenizer.md) class for a description
of the parameters.
<br /><br /><br />


<a name="normalize"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">normalize</strong>(stopwords=True,
custom_stopwords=None, stem=False, lemmatize=True)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/nlp.py#L1269">[source]</a>
</span>
</div>
Convert words to a more uniform standard. The transformations are
applied on the column named `Corpus`, in the same order the parameters
are presented. If there is no column with that name, an exception is
raised. See the [Normalizer](../nlp/normalizer.md) class for a
description of the parameters.
<br /><br /><br />


<a name="vectorize"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">vectorize</strong>(strategy="BOW", **kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/nlp.py#L1300">[source]</a>
</span>
</div>
Transform the corpus into meaningful vectors of numbers. The
transformation is applied on the column named `Corpus`. If there
is no column with that name, an exception is raised. See the
[Vectorizer](../nlp/vectorizer.md) class for a description of
the parameters.
<br /><br /><br />



## Feature engineering

To further pre-process the data, it's possible to extract features
from datetime columns, create new non-linear features transforming
the existing ones or, if the dataset is too large, remove features
using one of the provided strategies.

<table style="font-size:16px;margin-top:5px">
<tr>
<td><a href="#feature-extraction">feature_extraction</a></td>
<td>Extract features from datetime columns.</td>
</tr>

<tr>
<td><a href="#feature-generation">feature_generation</a></td>
<td>Create new features from combinations of existing ones.</td>
</tr>

<tr>
<td><a href="#feature-selection">feature_selection</a></td>
<td>Remove features according to the selected strategy.</td>
</tr>
</table>
<br>


<a name="feature-extraction"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">feature_extraction</strong>(features=["day", "month", "year"],
fmt=None, encoding_type="ordinal", drop_columns=True)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L1324">[source]</a>
</span>
</div>
Extract features (hour, day, month, year, etc..) from datetime columns.
Columns of dtype `datetime64` are used as is. Categorical columns that
can be successfully converted to a datetime format (less than 30% NaT
values after conversion) are also used. See the [FeatureExtractor](../feature_engineering/feature_extractor.md) class for a
description of the parameters.
<br /><br /><br />


<a name="feature-generation"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">feature_generation</strong>(strategy="DFS",
n_features=None, generations=20, population=500, operators=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L1357">[source]</a>
</span>
</div>
Use Deep feature Synthesis or a genetic algorithm to create new
combinations of existing features to capture the non-linear relations
between the original features. See [FeatureGenerator](../feature_engineering/feature_generator.md)
for a description of the parameters. Attributes created by the class
are attached to atom.
<br /><br /><br />


<a name="feature-selection"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">feature_selection</strong>(strategy=None,
solver=None, n_features=None, max_frac_repeated=1., max_correlation=1., **kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L1396">[source]</a>
</span>
</div>
Remove features according to the selected strategy. Ties between
features with equal scores are broken in an unspecified way. Also
removes features with too low variance and finds pairs of collinear
features based on the Pearson correlation coefficient. For each pair
above the specified limit (in terms of absolute value), it removes
one of the two. See [FeatureSelector](../feature_engineering/feature_selector.md)
for a description of the parameters. Plotting methods and attributes
created by the class are attached to atom.

!!! note
    <ul style="line-height:1.2em;margin-top:5px">
    <li>When strategy="univariate" and solver=None, [f_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html)
        is used as default solver.</li>
    <li>When strategy is one of SFM, RFE, RFECV or SFS and the solver is one of 
        ATOM's [predefined models](../../../user_guide/models/#predefined-models), the
        algorithm automatically selects the regressor (no need to add `_reg`
        to the solver).</li>
    <li>When strategy is one of SFM, RFE, RFECV or SFS and solver=None, atom
         uses the winning model (if it exists) as solver.</li>
    <li>When strategy is RFECV or SFS and no scoring is specified, atom uses the
        metric in the pipeline (if it exists) as scoring parameter.</li>

<br /><br />



## Training

The training methods are where the models are fitted to the data and
their performance is evaluated according to the selected metric. There
are three methods to call the three different training approaches in
ATOM. All relevant attributes and methods from the training classes are
attached to atom for convenience. These include the errors, winner and
results attributes, as well as the [models](../../../user_guide/models),
and the [prediction](../../../user_guide/predicting) and
[plotting](../../../user_guide/plots) methods.

<table style="font-size:16px;margin-top:5px">
<tr>
<td><a href="#run">run</a></td>
<td>Fit the models to the data in a direct fashion.</td>
</tr>

<tr>
<td><a href="#successive-halving">successive_halving</a></td>
<td>Fit the models to the data in a successive halving fashion.</td>
</tr>

<tr>
<td><a href="#train-sizing">train_sizing</a></td>
<td>Fit the models to the data in a train sizing fashion.</td>
</tr>
</table>
<br>


<a name="run"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">run</strong>(models=None,
metric=None, greater_is_better=True, needs_proba=False, needs_threshold=False,
n_calls=10, n_initial_points=5, est_params=None, bo_params=None, n_bootstrap=0)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L1537">[source]</a>
</span>
</div>
Fit and evaluate the models. The following steps are applied to every model:

1. Hyperparameter tuning is performed using a Bayesian Optimization
   approach (optional).
2. The model is fitted on the training set using the best combination
   of hyperparameters found.
3. The model is evaluated on the test set.
4. The model is trained on various bootstrapped samples of the training
   set and scored again on the test set (optional).

See [DirectClassifier](../training/directclassifier.md) for a description of
the parameters.
<br /><br /><br />


<a name="successive-halving"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">successive_halving</strong>(models=None,
metric=None, greater_is_better=True, needs_proba=False, needs_threshold=False,
skip_runs=0, n_calls=0, n_initial_points=5, est_params=None, bo_params=None,
n_bootstrap=0)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L1576">[source]</a>
</span>
</div>
Fit and evaluate the models in a [successive halving](../../../user_guide/training/#successive-halving)
fashion. The following steps are applied to every model (per iteration):

1. Hyperparameter tuning is performed using a Bayesian Optimization
   approach (optional).
2. The model is fitted on the training set using the best combination
   of hyperparameters found.
3. The model is evaluated on the test set.
4. The model is trained on various bootstrapped samples of the training
   set and scored again on the test set (optional).

See [SuccessiveHalvingClassifier](../training/successivehalvingclassifier.md)
for a description of the parameters.
<br /><br /><br />


<a name="train-sizing"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">train_sizing</strong>(models=None,
metric=None, greater_is_better=True, needs_proba=False, needs_threshold=False,
train_sizes=5, n_calls=0, n_initial_points=5, est_params=None, bo_params=None,
n_bootstrap=0)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/atom.py#L1622">[source]</a>
</span>
</div>
Fit and evaluate the models in a [train sizing](../../../user_guide/training/#train-sizing)
fashion. The following steps are applied to every model (per iteration):

1. Hyperparameter tuning is performed using a Bayesian Optimization
   approach (optional).
2. The model is fitted on the training set using the best combination
   of hyperparameters found.
3. The model is evaluated on the test set.
4. The model is trained on various bootstrapped samples of the training
   set and scored again on the test set (optional).

See [TrainSizingClassifier](../training/trainsizingclassifier.md) for a
description of the parameters.
<br /><br /><br />



## Example

```python
from atom import ATOMRegressor

# Initialize atom
atom = ATOMRegressor(X, y, logger="auto", n_jobs=2, verbose=2)

# Apply data cleaning methods
atom.prune(strategy="iforest", include_target=True)

# Fit the models to the data
atom.run(
    models=["OLS", "BR", "CatB"],
    metric="MSE",
    n_calls=25,
    n_initial_points=10,
    n_bootstrap=4,
)

# Analyze the results
atom.plot_errors(figsize=(9, 6), filename="errors.png")  
atom.catb.plot_feature_importance(filename="catboost_feature_importance.png")

# Get the predictions for the best model on new data
pred = atom.predict(X_new)
```