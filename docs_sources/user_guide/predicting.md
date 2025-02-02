# Predicting
------------

After running a successful pipeline, it's possible you would like to
apply all used transformations onto new data, or make predictions using
one of the trained models. Just like a sklearn estimator, you can call
the prediction methods from a fitted trainer, e.g. `atom.predict(X)`.
Calling the method without specifying a model will use the winning model
in the pipeline (under attribute `winner`). To use a different model,
simply call the method from a model, e.g. `atom.AdaB.predict(X)`.

All prediction methods transform the provided data through all
transformers in the current branch before making the predictions.
By default, this excludes transformers that should only be applied
on the training set, like outlier pruning and balancing the dataset.
Use the method's `pipeline` parameter to customize which
transformations to apply with every call.

The available prediction methods are a selection of the most common
methods for estimators in sklearn's API:

<table>
<tr>
<td><a href="../../API/predicting/transform">transform</a></td>
<td>Transform new data through all transformers in a branch.</td>
</tr>

<tr>
<td><a href="../../API/predicting/predict">predict</a></td>
<td>Return class predictions.</td>
</tr>

<tr>
<td><a href="../../API/predicting/predict_proba">predict_proba</a></td>
<td>Return class probabilities.</td>
</tr>

<tr>
<td><a href="../../API/predicting/predict_log_proba">predict_log_proba</a></td>
<td>Return class log-probabilities. </td>
</tr>

<tr>
<td><a href="../../API/predicting/decision_function">decision_function</a></td>
<td>Return confidence scores.</td>
</tr>

<tr>
<td><a href="../../API/predicting/score">score</a></td>
<td>Return a metric score.</td>
</tr>
</table>

Except for transform, the prediction methods can be calculated on the
train and test set. You can access them through the model's **prediction
attributes**, e.g. `atom.mnb.predict_train` or ` atom.mnb.predict_test`.
Keep in mind that the results are not calculated until the attribute is
called for the first time. This mechanism avoids having to calculate
attributes that are never used, saving time and memory.

Except for transform and score, it's possible to get the prediction on a
specific row or rows in the dataset providing their index names or positions,
e.g. `atom.rf.predict(10)` returns the random forest's prediction on the
10th row in the dataset, or `atom.rf.predict_proba(["index1", "index2"])`
returns the model's class probabilities for the rows in the dataset with
indices `index1` and `index2`.


!!! note
    Many of the [plots](../plots) use the prediction attributes. This can
    considerably increase the size of the instance for large datasets. Use
    the [clear](../../API/ATOM/atomclassifier/#clear) method if you need to
    free some memory!

