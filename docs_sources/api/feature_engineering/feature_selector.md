# FeatureSelector
-----------------

<div style="font-size:20px">
<em>class</em> atom.feature_engineering.<strong style="color:#008AB8">FeatureSelector</strong>(strategy=None,
solver=None, n_features=None, max_frac_repeated=1., max_correlation=1., n_jobs=1, verbose=0, logger=None, random_state=None,
**kwargs)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/feature_engineering.py#L571">[source]</a>
</span>
</div>

Remove features according to the selected strategy. Ties between
features with equal scores are broken in an unspecified way.
Additionally, removes features with too low variance and finds pairs of
collinear features based on the Pearson correlation coefficient. For
each pair above the specified limit (in terms of absolute value), it
removes one of the two. This class can be accessed from atom
through the [feature_selection](../../ATOM/atomclassifier/#feature-selection)
method. Read more in the [user guide](../../../user_guide/feature_engineering/#selecting-useful-features).

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<strong>strategy: string or None, optional (default=None)</strong><br>
Feature selection strategy to use. Choose from:
<ul style="line-height:1.2em;margin-top:5px">
<li>None: Do not perform any feature selection algorithm.</li>
<li>"univariate": Univariate F-test.</li>
<li>"PCA": Principal Component Analysis.</li>
<li>"SFM": Select best features according to a model.</li>
<li>"SFS": Sequential Feature Selection.</li>
<li>"RFE": Recursive Feature Elimination.</li>
<li>"RFECV": RFE with cross-validated selection.</li>
</ul>
<strong>solver: string, estimator or None, optional (default=None)</strong><br>
Solver or model to use for the feature selection strategy. See
sklearn's documentation for an extended description of the choices.
Select None for the default option per strategy (only for univariate
and PCA).
<ul style="line-height:1.2em;margin-top:5px">
<li>for "univariate", choose from:
    <ul style="line-height:1.2em;margin-top:5px">
    <li>"f_classif"</li>
    <li>"f_regression"</li>
    <li>"mutual_info_classif"</li>
    <li>"mutual_info_regression"</li>
    <li>"chi2"</li>
    <li>Any function taking two arrays (X, y), and returning
        arrays (scores, p-values). See the sklearn <a href="https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection">documentation</a>.</li>
    </ul></li>
<li>for "PCA", choose from:
    <ul style="line-height:1.2em;margin-top:5px">
    <li>"auto" (default)</li>
    <li>"full"</li>
    <li>"arpack"</li>
    <li>"randomized"</li>
    </ul></li>
<li>for "SFM", "SFS", "RFE" and "RFECV":<br>
<p>The base estimator. For SFM, RFE and RFECV, it should
have either a either a <code>feature_importances_</code> or <code>coef_</code>
attribute after fitting. You can use one of ATOM's <a href="../../../user_guide/models/#predefined-models">predefined models</a>.
Add <code>_class</code> or <code>_reg</code> after the model's name to
specify a classification or regression task, e.g. <code>solver="LGB_reg"</code>
(not necessary if called from an atom instance). No default option.</p></li>
</ul>
<strong>n_features: int, float or None, optional (default=None)</strong><br>
Number of features to select. Choose from:
<ul style="line-height:1.2em;margin-top:5px;margin-bottom:0">
<li>if None: Select all features.</li>
<li>if < 1: Fraction of the total features to select.</li>
<li>if >= 1: Number of features to select.</li>
</ul>
<p style="margin-top:5px">
If strategy="SFM" and the threshold parameter is not specified, the
threshold is set to <code>-np.inf</code> to select the <code>n_features</code>
features. If strategy="RFECV", it's the minimum number of features to select.
</p>
<strong>max_frac_repeated: float or None, optional (default=1.)</strong><br>
Remove features with the same value in at least this fraction of
the total rows. The default is to keep all features with non-zero
variance, i.e. remove the features that have the same value in all
samples. If None, skip this step.
<p>
<strong>max_correlation: float or None, optional (default=1.)</strong><br>
Minimum value of the Pearson correlation coefficient to identify
correlated features. A value of 1 removes one of 2 equal columns.
A dataframe of the removed features and their correlation values can
be accessed through the collinear attribute. If None, skip this step.
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
<p>
<strong>**kwargs</strong><br>
Any extra keyword argument for the PCA, SFM, RFE, RFECV  and SFS estimators.
See the corresponding sklearn documentation for the available options.
</p>
</td>
</tr>
</table>

!!! info
    If strategy="PCA", the data is scaled to mean=0 and std=1 before
    fitting the transformer (if it wasn't already).

!!! tip
    Use the [plot_feature_importance](../plots/plot_feature_importance.md) method to
    examine how much a specific feature contributes to the final predictions. If the
    model doesn't have a `feature_importances_` attribute, use 
    [plot_permutation_importance](../plots/plot_permutation_importance.md) instead.

!!! warning
    The RFE, RFECV AND SFS strategies don't work when the solver is a 
    [CatBoost](https://catboost.ai/) model due to incompatibility of the APIs.

<br>



## Attributes

### Utility attributes

<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Attributes:</strong></td>
<td width="80%" class="td_params">
<strong>collinear: pd.DataFrame</strong><br>
Information on the removed collinear features. Columns include:
<ul style="line-height:1.2em;margin-top:5px">
<li><b>drop_feature:</b> Name of the feature dropped by the method.</li>
<li><b>correlated feature:</b> Name of the correlated feature(s).</li>
<li><b>correlation_value:</b> Pearson correlation coefficients of the feature pairs.</li>
</ul>
<p>
<strong>feature_importance: list</strong><br>
Remaining features ordered by importance. Only if strategy in ("univariate", "SFM,
"RFE", "RFECV"). For RFE and RFECV, the importance is extracted from the external
estimator fitted on the reduced set. 
</p>
<p>
<strong>&lt;strategy&gt;: sklearn transformer</strong><br>
Object (lowercase strategy) used to transform the data,
e.g. <code>feature_selector.pca</code> for the PCA strategy.
</p>
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
<br><br><br>



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
<td><a href="#plot-pca">plot_pca</a></td>
<td>Plot the explained variance ratio vs the number of components.</td>
</tr>

<tr>
<td><a href="#plot-components">plot_components</a></td>
<td>Plot the explained variance ratio per component.</td>
</tr>

<tr>
<td><a href="#plot-rfecv">plot_rfecv</a></td>
<td>Plot the scores obtained by the estimator on the RFECV.</td>
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
<em>method</em> <strong style="color:#008AB8">fit</strong>(X, y=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/feature_engineering.py#L730">[source]</a>
</span>
</div>
Fit to data. Note that the univariate, SFM (when model is not fitted),
SFS, RFE and RFECV strategies all need a target column. Leaving it
None will raise an exception.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>X: dataframe-like</strong><br>
Feature set with shape=(n_samples, n_features).
</p>
<strong>y: int, str, sequence or None, optional (default=None)</strong><br>
<ul style="line-height:1.2em;margin-top:5px">
<li>If None: y is ignored.</li>
<li>If int: Index of the target column in X.</li>
<li>If str: Name of the target column in X.</li>
<li>Else: Target column with shape=(n_samples,).</li>
</ul>
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>self: FeatureSelector</strong><br>
Fitted instance of self.
</tr>
</table>
<br />


<a name="fit-transform"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">fit_transform</strong>(X, y=None)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/data_cleaning.py#L74">[source]</a>
</span>
</div>
Fit to data, then transform it. Note that the univariate, SFM (when
model is not fitted), SFS, RFE and RFECV strategies need a target column.
Leaving it None will raise an exception.
<table style="font-size:16px">
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Parameters:</strong></td>
<td width="80%" class="td_params">
<p>
<strong>X: dataframe-like</strong><br>
Feature set with shape=(n_samples, n_features).
</p>
<strong>y: int, str, sequence or None, optional (default=None)</strong><br>
<ul style="line-height:1.2em;margin-top:5px">
<li>If None: y is ignored.</li>
<li>If int: Index of the target column in X.</li>
<li>If str: Name of the target column in X.</li>
<li>Else: Target column with shape=(n_samples,).</li>
</ul>
</tr>
<tr>
<td width="20%" class="td_title" style="vertical-align:top"><strong>Returns:</strong></td>
<td width="80%" class="td_params">
<strong>X: pd.DataFrame</strong><br>
Transformed feature set.
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


<a name="plot-pca"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">plot_pca</strong>
(title=None, figsize=(10, 6), filename=None, display=True)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/plots.py#L497">[source]</a>
</span>
</div>
Plot the explained variance ratio vs the number of components.
See [plot_pca](../../plots/plot_pca) for a description of the parameters.
<br /><br /><br />


<a name="plot-components"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">plot_components</strong>
(show=None, title=None, figsize=None, filename=None, display=True)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/plots.py#L567">[source]</a>
</span>
</div>
Plot the explained variance ratio per components. See
[plot_components](../../plots/plot_components) for a description of the parameters.
<br /><br /><br />


<a name="plot-rfecv"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">plot_rfecv</strong>
(title=None, figsize=(10, 6), filename=None, display=True)
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/plots.py#L644">[source]</a>
</span>
</div>
Plot the scores obtained by the estimator fitted on every subset of the
data. See [plot_rfecv](../../plots/plot_rfecv) for a description of the parameters.
<br /><br /><br />


<a name="reset-aesthetics"></a>
<div style="font-size:20px">
<em>method</em> <strong style="color:#008AB8">reset_aesthetics</strong>()
<span style="float:right">
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/plots.py#L221">[source]</a>
</span>
</div>
Reset the [plot aesthetics](../../../user_guide/plots/#aesthetics) to their default values.
<br /><br /><br />


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
<a href="https://github.com/tvdboom/ATOM/blob/master/atom/feature_engineering.py#L987">[source]</a>
</span>
</div>
Transform the data.
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
Transformed feature set.
</tr>
</table>
<br />



## Example

```python
from atom import ATOMClassifier

atom = ATOMClassifier(X, y)
atom.feature_selection(stratgey="pca", n_features=12, whiten=True)

atom.plot_pca(filename="pca", figsize=(8, 5))
```
or
```python
from atom.feature_engineering import FeatureSelector

feature_selector = FeatureSelector(stratgey="pca", n_features=12, whiten=True)
feature_selector.fit(X_train, y_train)
X = feature_selector.transform(X, y)

feature_selector.plot_pca(filename="pca", figsize=(8, 5))
```