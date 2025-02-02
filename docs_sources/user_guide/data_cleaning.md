# Data cleaning
---------------

More often than not, you'll need to do some data cleaning before fitting
your dataset to a model.  Usually, this involves importing different
libraries and writing many lines of code. Since ATOM is all about fast
exploration  and experimentation, it provides various data cleaning
classes to apply the most common transformations fast and easy.

!!! note
    All of atom's data cleaning methods automatically adopt the relevant
    transformer attributes (`n_jobs`, `verbose`, `logger`, `random_state`) from
    atom. A different choice can be added as parameter to the method call,
    e.g. `atom.scale(verbose=2)`.

!!! note
    Like the [add](../../API/ATOM/atomclassifier/#add) method, the data cleaning
    methods accept the `columns` parameter to only transform a subset of the
    dataset's features, e.g. `atom.scale(columns=[0, 1])`.


<br>

## Scaling the feature set

Standardization of a dataset is a common requirement for many machine
learning estimators; they might behave badly if the individual features
do not more or less look like standard normally distributed data (e.g.
Gaussian with zero mean and unit variance). The [Scaler](../../API/data_cleaning/scaler)
class let you quickly scale atom's dataset using one of sklearn's scalers.
It can be accessed from atom through the [scale](../../API/ATOM/atomclassifier/#scale)
method. 

!!! tip
    Use atom's [scaled](../../API/ATOM/atomclassifier/#data-attributes) attribute
    to check whether the dataset is scaled.

<br>

## Making Gaussian-like features

Use the [Gauss](../../API/data_cleaning/gauss) class to transform the
feature set to follow a Gaussian-like (or normal) distribution. In
general, data must be transformed when using models that assume
normality in the residuals. Examples of such models are
[Logistic Regression](../../API/models/lr), [Linear Discriminant Analysis](../../API/models/lda)
and [Gaussian Naive Bayes](../../API/models/gnb). The class can be
accessed from atom through the [gauss](../../API/ATOM/atomclassifier/#gauss)
method.

!!! tip
    Use atom's [plot_distribution](../../API/plots/plot_distribution) method
    to examine a column's distribution.

<br>

## Standard data cleaning

There are many data cleaning steps that are useful to perform on any
dataset before modelling. These are general rules that apply almost
on every use-case and every task. The [Cleaner](../../API/data_cleaning/cleaner)
class is a convenient tool to apply such steps. It can be accessed
from atom through the [clean](../../API/ATOM/atomclassifier/#clean)
method. Use the class' parameters to choose which transformations to
perform. The available steps are:

* Drop columns with specific data types.
* Strip categorical features from white spaces.
* Drop categorical columns with maximal cardinality.
* Drop columns with minimum cardinality.
* Drop duplicate rows.
* Drop rows with missing values in the target column.
* Encode the target column.

<br>

## Imputing missing values

For various reasons, many real world datasets contain missing values,
often encoded as blanks, NaNs or other placeholders. Such datasets
however are incompatible with ATOM's models which assume that all
values in an array are numerical, and that all have and hold meaning.
The [Imputer](../../API/data_cleaning/imputer) class handles missing
values in the dataset by either dropping or imputing the value. It can 
be accessed from atom through the [impute](../../API/ATOM/atomclassifier/#impute)
method.

!!! tip
    Use atom's [missing](../../API/ATOM/atomclassifier/#data-attributes) attribute
    to check the amount of missing values per column.

<br>

## Encoding categorical features

Many datasets contain categorical features. Their variables are
typically stored as text values which represent various classes.
Some examples include color (“Red”, “Yellow”, “Blue”), size (“Small”,
“Medium”, “Large”) or geographic designations (city or country).
Regardless of what the value is used for, the challenge is determining
how to use this data in the analysis. The majority of sklearn's models
don't support direct manipulation of this kind of data. Use the
[Encoder](../../API/data_cleaning/encoder) class to encode categorical
features to numerical values. It can be  accessed from atom through the
[encode](../../API/ATOM/atomclassifier/#encode) method.

There are many strategies to encode categorical columns. The Encoder
class applies one strategy or another depending on the number of
classes in the column to be encoded. When there are only two, the values
are encoded with 0 or 1. When there are more than two, the columns can
be encoded using one-hot encoding or any other strategy of the
[category-encoders](https://contrib.scikit-learn.org/category_encoders/)
package, depending on the value of the `max_onehot` parameter.
[One-hot](https://contrib.scikit-learn.org/category_encoders/onehot.html)
encodes the column making a dummy feature for every class. This
approach preserves all the information but increases the size of
the dataset considerably, making it often an undesirable strategy for
high cardinality features. Other strategies like [LeaveOneOut](https://contrib.scikit-learn.org/category_encoders/leaveoneout.html)
transform the column in place.

!!! tip
    Use atom's [categorical](../../API/ATOM/atomclassifier/#data-attributes)
    attribute for a list of the categorical features in the dataset.

<br>

## Handling outliers

When modelling, it is important to clean the data sample to ensure that
the observations best represent the problem. Sometimes a dataset can
contain extreme values that are outside the range of what is expected
and unlike the other data. These are called outliers. Often, machine
learning modelling and model skill in general can be improved by 
understanding and even removing these outlier samples. The [Pruner](../../API/data_cleaning/pruner) 
class offers 7 different strategies to detect outliers (described
hereunder). It can be accessed from atom through the [prune](../../API/ATOM/atomclassifier/#prune)
method.

!!! tip
    Use atom's [outliers](../../API/ATOM/atomclassifier/#data-attributes) attribute
    to check the number of outliers per column.


**z-score**<br>
The z-score of a value in the dataset is defined as the number of standard
deviations by which the value is above or below the mean of the column.
Values above or below a certain threshold (specified with the parameter
`max_sigma`) are considered outliers. Note that, contrary to the rest of
the strategies, this approach selects outlier values, not outlier samples!
Because of this, it is possible to replace the outlier value instead of
dropping the entire sample.


**Isolation Forest**<br>
Uses a tree-based anomaly detection algorithm. It is based
on modeling the normal data in such a way as to isolate anomalies that are
both few and different in the feature space. Read more in sklearn's [documentation](https://scikit-learn.org/stable/modules/outlier_detection.html#isolation-forest).


**Elliptic Envelope**<br>
If the input variables have a Gaussian distribution, then simple statistical
methods can be used to detect outliers. For example, if the dataset has two
input variables and both are Gaussian, the feature space forms a
multi-dimensional Gaussian, and knowledge of this distribution can be used to
identify values far from the distribution. This approach can be generalized by
defining a hypersphere (ellipsoid) that covers the normal data, and data that
falls outside this shape is considered an outlier. Read more in sklearn's [documentation](https://scikit-learn.org/stable/modules/outlier_detection.html#fitting-an-elliptic-envelope).


**Local Outlier Factor**<br>
A simple approach to identifying outliers is to locate those examples that
are far from the other examples in the feature space. This can work well
for feature spaces with low dimensionality (few features) but becomes
less reliable as the number of features is increased. The local outlier
factor is a technique that attempts to harness the idea of nearest neighbors
for outlier detection. Each example is assigned a score of how isolated
or how likely it is to be outliers based on the size of its local
neighborhood. Those examples with the largest score are more likely to
be outliers. Read more in sklearn's [documentation](https://scikit-learn.org/stable/modules/outlier_detection.html#local-outlier-factor).


**One-class SVM**<br>
The support vector machine algorithm, initially developed for binary
classification tasks, can also be used for one-class classification.
When modeling one class, the algorithm captures the density of the
majority class and classifies examples on the extremes of the density
function as outliers. This modification of SVM is referred to as
One-Class SVM. Read more in sklearn's [documentation](https://scikit-learn.org/stable/modules/outlier_detection.html#novelty-detection).


**DBSCAN**<br>
The DBSCAN algorithm views clusters as areas of high density separated by
areas of low density. Due to this rather generic view, clusters found by
DBSCAN can be any shape, as opposed to k-means which assumes that clusters
are convex shaped. Samples that lie outside any cluster are considered outliers.
Read more in sklearn's [documentation](https://scikit-learn.org/stable/modules/clustering.html#dbscan).


**OPTICS**<br>
The OPTICS algorithm shares many similarities with the DBSCAN algorithm,
and can be considered a generalization of DBSCAN that relaxes the `eps`
requirement from a single value to a value range. The key difference
between DBSCAN and OPTICS is that the OPTICS algorithm builds a reachability
graph, and a spot within the cluster ordering. These two attributes are
assigned when the model is fitted, and are used to determine cluster
membership. Read more in sklearn's [documentation](https://scikit-learn.org/stable/modules/clustering.html#optics).


<br>

## Balancing the data

One of the common issues found in datasets that are used for
classification is imbalanced classes. Data imbalance usually reflects
an unequal distribution of classes within a dataset. For example, in
a credit card fraud detection dataset, most of the transactions are
non-fraud, and a very few cases are fraud. This leaves us with a very
unbalanced ratio of fraud vs non-fraud cases. The [Balancer](../../API/data_cleaning/balancer)
class can oversample the minority class or undersample the majority
class using any of the transformers implemented in the
[imblearn](https://imbalanced-learn.org/stable/index.html) package. It
can be  accessed from atom through the [balance](../../API/ATOM/atomclassifier/#balance)
method.


