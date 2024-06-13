# Overview
이 폴더는 캐글의 [American Express - Default Prediction](https://www.kaggle.com/competitions/amex-default-prediction) 대회에서 사용한 데이터를 XGBoost 모델로 학습시켜 성능이 좋아 지능 과정의 모든 코드를 담고 있습니다.

# Submission
최종적으로 제출한 결과는 다음과 같습니다.
### Submission 결과
> 첫번째 제출은 범주형 데이터를 Label Encoding을 통해 변환하고, 수치형 데이터를 XGBoost 모델로 학습시켜 제출한 결과입니다.
- [1st submission](https://github.com/SUNGMYEONGGI/ML-project-to-fastcampus/blob/main/XGBoost/AMEX_XGBoost_1submit.ipynb)
  - Public Score: 0.77687
  - Private Score: 0.78558

> 두번째 제출은 첫번째 결과를 통해 얻어진 Top30 Feature Importance를 통해 Top30의 Feature만의 컬럼을 사용하여 모델을 재학습시켜 제출한 결과입니다.
- [2nd submission](https://github.com/SUNGMYEONGGI/ML-project-to-fastcampus/blob/main/XGBoost/AMEX_Top30_FeatureImportance.ipynb)
  - Public Score: 0.76225
  - Private Score: 0.77557

> 세번째 제출은 범주형 데이터를 One-Hot Encoding을 통해 변환하고, 수치형 데이터를 중앙값으로 채워 XGBoost 모델로 학습시켜 제출한 결과입니다.
- [3nd submission](https://github.com/SUNGMYEONGGI/ML-project-to-fastcampus/blob/main/XGBoost/AMEX_XGBoost_2submit.ipynb)
  - Public Score: 0.77455
  - Private Score: 0.78297

> 네번째 제출은 1st+3rd submission을 통해 얻어진 결과를 앙상블하여 Soft Voting을 통해 제출한 결과입니다.
- 4th submission
  - Public Score: 0.78133
  - Private Score: 0.79000

# Reference & Link
- https://www.kaggle.com/code/cdeotte/xgboost-starter-0-793