# FeatureGenerator
------------------

<div style="font-size:20px">
<em>class</em> atom.feature_engineering.<strong style="color:#008AB8">FeatureGenerator</strong>(strategy="DFS",
n_features=None, generations=20, population=500, operators=None,
n_jobs=1, verbose=0, logger=None, random_state=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/feature_engineering.py#L231">[source]</a>
</span>
</div>

Use Deep feature Synthesis or a genetic algorithm to create new combinations
of existing features to capture the non-linear relations between the original
features. This class can be accessed from atom through the
[feature_generation](../../ATOM/atomclassifier/#feature-generation)
method. Read more in the [user guide](../../../user_guide/feature_engineering/#generating-new-features).

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<strong>strategy: str, optional (default="DFS")</strong><br>
Strategy to crate new features. Choose from:
<ul style="line-height:1.2em;margin-top:5px">
<li>"DFS" to use Deep Feature Synthesis.</li>
<li>"GFG" or "genetic" to use Genetic Feature Generation.</li>
</ul>
<p>
<strong>n_features: int or None, optional (default=None)</strong><br>
Number of newly generated features to add to the dataset (no
more than 1% of the population for the genetic strategy). If
None, select all created features.
</p>
<p>
<strong>generations: int, optional (default=20)</strong><br>
Number of generations to evolve. Only for the genetic strategy.
</p>
<p>
<strong>population: int, optional (default=500)</strong><br>
Number of programs in each generation. Only for the genetic strategy.
</p>
<p>
<strong>operators: str, list, tuple or None, optional (default=None)</strong><br>
Name of the operators to be used on the features. None to use all.
Choose from: add, sub, mul, div, sqrt, log, sin, cos, tan.
</p>
<strong>n_jobs: int, optional (default=1)</strong><br>
Number of cores to use for parallel processing.
<ul style="line-height:1.2em;margin-top:5px">
<li>If >0: Number of cores to use.</li>
<li>If -1: Use all available cores.</li>
<li>If <-1: Use available_cores - 1 + <code>n_jobs</code>.</li>
</ul>
<strong>verbose: int, optional (default=0)</strong><br>
Verbosity level of the class. Possible values are:
<ul style="line-height:1.2em;margin-top:5px">
<li>0 to not print anything.</li>
<li>1 to print basic information.</li>
<li>2 to print detailed information.</li>
</ul>
<strong>logger: str, Logger or None, optional (default=None)</strong><br>
<ul style="line-height:1.2em;margin-top:5px">
<li>If None: Doesn't save a logging file.</li>
<li>If str: Name of the log file. Use "auto" for automatic naming.</li>
<li>Else: Python <code>logging.Logger</code> instance.</li>
</ul>
<strong>random_state: int or None, optional (default=None)</strong><br>
Seed used by the random number generator. If None, the random number
generator is the <code>RandomState</code> instance used by <code>np.random</code>.
</td>
</tr>
</table>


!!! tip
    DFS can create many new features and not all of them will be useful. Use
    [FeatureSelector](/API/feature_engineering/feature_selector) to reduce
    the number of features!

!!! warning
    Using the div, log or sqrt operators can return new features with `inf` or
    `NaN` values. Check the warnings that may pop up or use atom's
    [missing](/API/ATOM/atomclassifier/#data-attributes) property.

!!! warning
    When using DFS with `n_jobs>1`, make sure to protect your code with `if __name__
    == "__main__"`. Featuretools uses [dask](https://dask.org/), which uses python
    multiprocessing for parallelization. The spawn method on multiprocessing starts
    a new python process, which requires it to import the \__main__ module before it
    can do its task.

<br>

## Attributes

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Attributes:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>symbolic_transformer: <a href="https://gplearn.readthedocs.io/en/stable/reference.html#symbolic-transformer">SymbolicTransformer</a></strong><br>
Object used to calculate the genetic features. Only for the genetic strategy.
</p>
<strong>genetic_features: pd.DataFrame</strong><br>
Information on the newly created non-linear features. Only for the genetic
strategy. Columns include:
<ul style="line-height:1.2em;margin-top:5px">
<li><b>name:</b> Name of the feature (automatically created).</li>
<li><b>description:</b> Operators used to create this feature.</li>
<li><b>fitness:</b> Fitness score.</li>
</ul>
</td>
</tr>
</table>
<br>



## Methods

<table style="font-size:16px">
<tr>
<td><a href="#fit">fit</a></td>
<td>Fit to data.</td>
</tr>

<tr>
<td><a href="#fit-transform">fit_transform</a></td>
<td>Fit to data, then transform it.</td>
</tr>

<tr>
<td><a href="#get-params">get_params</a></td>
<td>Get parameters for this estimator.</td>
</tr>

<tr>
<td><a href="#log">log</a></td>
<td>Write information to the logger and print to stdout.</td>
</tr>

<tr>
<td><a href="#save">save</a></td>
<td>Save the instance to a pickle file.</td>
</tr>

<tr>
<td><a href="#set-params">set_params</a></td>
<td>Set the parameters of this estimator.</td>
</tr>

<tr>
<td><a href="#transform">transform</a></td>
<td>Transform the data.</td>
</tr>
</table>
<br>


<a name="fit"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">fit</strong>(X, y)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/feature_engineering.py#L328">[source]</a>
</span>
</div>
Fit to data.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>X: dataframe-like</strong><br>
Feature set with shape=(n_samples, n_features).
</p>
<strong>y: int, str or sequence</strong><br>
<ul style="line-height:1.2em;margin-top:5px">
<li>If int: Index of the target column in X.</li>
<li>If str: Name of the target column in X.</li>
<li>Else: Target column with shape=(n_samples,).</li>
</ul>
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>self: FeatureGenerator</strong><br>
Fitted instance of self.
</tr>
</table>
<br />


<a name="fit-transform"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">fit_transform</strong>(X, y)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/data_cleaning.py#L74">[source]</a>
</span>
</div>
Fit to data, then transform it.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>X: dataframe-like</strong><br>
Feature set with shape=(n_samples, n_features).
</p>
<strong>y: int, str or sequence</strong><br>
<ul style="line-height:1.2em;margin-top:5px">
<li>If int: Index of the target column in X.</li>
<li>If str: Name of the target column in X.</li>
<li>Else: Target column with shape=(n_samples,).</li>
</ul>
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>X: pd.DataFrame</strong><br>
Feature set with the newly generated features.
</tr>
</table>
<br />


<a name="get-params"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">get_params</strong>(deep=True)
<span style="float:right">
<a href="https://github.com/scikit-learn/scikit-learn/blob/0fb307bf3/sklearn/base.py#L189">[source]</a>
</span>
</div>
Get parameters for this estimator.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>deep: bool, optional (default=True)</strong><br>
If True, will return the parameters for this estimator and contained
subobjects that are estimators.
</p>
</td>
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>params: dict</strong><br>
Parameter names mapped to their values.
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


<a name="save"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">save</strong>(filename="auto")
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/basetransformer.py#L505">[source]</a>
</span>
</div>
Save the instance to a pickle file.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<strong>filename: str, optional (default="auto")</strong><br>
Name of the file. Use "auto" for automatic naming.
</td>
</tr>
</table>
<br>


<a name="set-params"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">set_params</strong>(**params)
<span style="float:right">
<a href="https://github.com/scikit-learn/scikit-learn/blob/0fb307bf3/sklearn/base.py#L221">[source]</a>
</span>
</div>
Set the parameters of this estimator.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<strong>**params: dict</strong><br>
Estimator parameters.
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>self: FeatureGenerator</strong><br>
Estimator instance.
</td>
</tr>
</table>
<br />


<a name="transform"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">transform</strong>(X, y=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/feature_engineering.py#L469">[source]</a>
</span>
</div>
Generate new features.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>X: dataframe-like</strong><br>
Feature set with shape=(n_samples, n_features).
</p>
<p>
<strong>y: int, str, sequence or None, optional (default=None)</strong><br>
Does nothing. Implemented for continuity of the API.
</p>
</td>
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>X: pd.DataFrame</strong><br>
Feature set with the newly generated features.
</tr>
</table>
<br />



## Example

```python
from atom import ATOMClassifier

atom = ATOMClassifier(X, y)
atom.feature_generation(strategy="genetic", n_features=3, generations=30)
```
or
```python
from atom.feature_engineering import FeatureGenerator

fg = FeatureGenerator(strategy="genetic", n_features=3, generations=30)
fg.fit(X_train, y_train)
X = fg.transform(X)
```