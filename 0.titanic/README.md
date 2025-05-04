# 0. titanic

* Note: This project is intended for submission as an assignment for the MLOps (2025-1) class.

* <details><summary>Assignment Submission Guideline</summary>

    * Due: 04/22 (Tue.) 23:59:59
    * Submissions: 3 files
        1. Source code 
            * `.py` or `.ipynb`
        2. requirements.txt 
        3. Reports 
            * around 3 pages, no more than 4 pages
            * free-format, but followings should be included
                1. Problem definition
                2. Dataset description
                3. Model description
                4. Evaluation methods and metrics (+ why it is important in your prob.?)
                5. Development environment (incl. OS, python, packages, …)
                6. Results & interpretation
                7. Link for the remote source repository (Github is recommended)
                8. (Optional) Scenarios for practical use

## Contents
1. [Problem definition](#problem-definition)
2. [Dataset description](#dataset-description)
3. [Model description](#model-description)
4. [Evaluation methods and metrics](#evaluation-methods-and-metrics)
5. [Development environment](#development-environment)
6. [Results & interpretation](#results--interpretation)
7. [Scenarios for practical use](#scenarios-for-practical-use)
8. Link for the remote source repository

## Problem definition
  먼저, 문제를 정의하기에 앞서, 수업 중에 알게 된 AutoML 패키지인 MLJAR를 사용했다. 이미 잘 알려진 타이타닉 데이터셋과 AutoML을 함께 사용한 이유는 사전에 알고 있는 지식과 AutoML이 산출해내는 결과값을 비교함으로써 베이스모델로서의 효능을 확인해보기 위해서였다.  
  AutoML의 학습 결과, logloss metric에 대해 ensemble 모델이 가장 뛰어난 성능을 보였다. 한편, neural network모델은 baseline 모델보다도 현저히 떨어지는 정확도를 기록했다. Xgboost, Random Forest, ensemble 모델에서 높은 성능을 달성한 것으로 보아 이는 데이터셋의 특성에서 비롯한 현상으로 볼 수 있다. 작은 규모, 정형화된 구조, 비선형 상호작용의 존재, 범주형 변수가 많다는 데이터셋의 특성 상 트리 기반 모델에서 좋은 성능을 보이는 한편 신경망 구성에서는 낮은 퍼포먼스를 보였던 것이다.

## Dataset description

## Model description

## Evaluation methods and metrics

## Development environment

## Results & interpretation

## Scenarios for practical use