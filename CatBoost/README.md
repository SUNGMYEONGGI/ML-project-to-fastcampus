# Overview
이 폴더는 캐글의 [American Express - Default Prediction](https://www.kaggle.com/competitions/amex-default-prediction) 대회에서 사용한 데이터를 CatBoost 모델로 학습시켜 성능이 좋아 지능 과정의 모든 코드를 담고 있습니다.

# Submission
최종적으로 제출한 결과는 다음과 같습니다.
### Submission 결과
> 첫번째 제출은 범주형 데이터를 LabelEncoding을 통해 수칫값으로 변환하고, 수치형 데이터를 중앙값으로 채워 CatBoost 모델로 학습시켜 제출한 결과입니다.
- 1st submission
  - Public Score: 0.77798
  - Private Score: 0.78789

> 두번째 제출은 범주형 데이터를 One-Hot Encoding을 통해 변환하고, 수치형 데이터를 0으로 채워 CatBoost 모델로 학습시켜 제출한 결과입니다.
- 2nd submission
  - Public Score: 0.77953
  - Private Score: 0.78892

> 세번째 제출은 1st+2nd submission을 통해 얻어진 결과를 앙상블하여 Soft Voting을 통해 제출한 결과입니다.
- 3nd submission
  - Public Score: 0.77934
  - Private Score: 0.78879

# Reference & Link
- https://www.kaggle.com/code/huseyincot/amex-catboost-0-793