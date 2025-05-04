# Summary of 5_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

1.8 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 1.09576  | nan           |
| auc       | 0.820089 | nan           |
| f1        | 0.736111 |   0.218557    |
| accuracy  | 0.786517 |   0.218557    |
| precision | 0.688312 |   0.218557    |
| recall    | 1        |   5.37792e-17 |
| mcc       | 0.562123 |   0.218557    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.09576  |  nan        |
| auc       | 0.820089 |  nan        |
| f1        | 0.736111 |    0.218557 |
| accuracy  | 0.786517 |    0.218557 |
| precision | 0.688312 |    0.218557 |
| recall    | 0.791045 |    0.218557 |
| mcc       | 0.562123 |    0.218557 |


## Confusion matrix (at threshold=0.218557)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               87 |               24 |
| Labeled as 1 |               14 |               53 |

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
