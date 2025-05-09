# Summary of 3_Linear

[<< Go back](../README.md)


## Logistic Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

1.4 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.597044 | nan           |
| auc       | 0.844023 | nan           |
| f1        | 0.758621 |   0.215787    |
| accuracy  | 0.803371 |   0.215787    |
| precision | 0.705128 |   0.215787    |
| recall    | 1        |   9.90277e-05 |
| mcc       | 0.599238 |   0.215787    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.597044 |  nan        |
| auc       | 0.844023 |  nan        |
| f1        | 0.758621 |    0.215787 |
| accuracy  | 0.803371 |    0.215787 |
| precision | 0.705128 |    0.215787 |
| recall    | 0.820896 |    0.215787 |
| mcc       | 0.599238 |    0.215787 |


## Confusion matrix (at threshold=0.215787)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               88 |               23 |
| Labeled as 1 |               12 |               55 |

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
