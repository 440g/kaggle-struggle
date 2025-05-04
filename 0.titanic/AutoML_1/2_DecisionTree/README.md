# Summary of 2_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 3
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

4.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.567493 |  nan        |
| auc       | 0.8373   |  nan        |
| f1        | 0.761194 |    0.134228 |
| accuracy  | 0.820225 |    0.134228 |
| precision | 0.761194 |    0.134228 |
| recall    | 0.985075 |    0        |
| mcc       | 0.61705  |    0.134228 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.567493 |  nan        |
| auc       | 0.8373   |  nan        |
| f1        | 0.761194 |    0.134228 |
| accuracy  | 0.820225 |    0.134228 |
| precision | 0.761194 |    0.134228 |
| recall    | 0.761194 |    0.134228 |
| mcc       | 0.61705  |    0.134228 |


## Confusion matrix (at threshold=0.134228)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               95 |               16 |
| Labeled as 1 |               16 |               51 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
