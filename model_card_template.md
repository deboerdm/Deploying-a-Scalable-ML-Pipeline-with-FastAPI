# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model in use here is the RandomForestClassifier from scikit-learn version 1.5.1, using default hyperparameters.



## Intended Use

This model is intended to ptedict whether or not an individual earns over $50K annually based on number of attributes provided by US Census data.

## Training Data

The census data used here was obtained from the UCI Machine learning Repository (https://archive.ics.uci.edu/dataset/20/census+income).  The original data set contained 32,561 rows and 15 columns comprised of 1 target label, 8 categorical features, and 6 numberical features.  Information on each of the features is available at the UCI link above.  The target label, "salary", has two options: "<=50K" or ">50K".  No data cleaning was performed on original data provided.

A 80/20 split was done to break the dataset into in training and test sets.  OneHotEncoder was used on the categorical features and LabelBinarizer used on the label feature.


## Evaluation Data

20 percent of the data was set aside to be used for testing.  OneHotEncoder and LabelBinarizer was applied to transform the same features as with the training data.

## Metrics

Model Performance:
- Precision: 0.7245
- Recall: 0.6182
- F1: 0.6671


## Ethical Considerations

The model is trained on US census data.  This model should not be used to assume salary levels of individuals in the current economy and present day.

## Caveats and Recommendations

The dataset is derived from US Census data from 1994.  The data is outdated and should not be used as a valid representation of the population anymore.  