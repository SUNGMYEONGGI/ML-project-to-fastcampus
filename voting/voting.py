import pandas as pd

# 세 개의 제출 파일 경로
file1_path = ''
file2_path = ''
file3_path = ''

# 제출 파일들 읽기
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
df3 = pd.read_csv(file3_path)

# 세 개의 예측값 평균 계산 (소프트 보팅)
df1['prediction'] = (df1['prediction'] + df2['prediction'] + df3['prediction']) / 3

# 최종 제출 파일 저장
output_path = 'ensemble_submission(soft).csv'
df1.to_csv(output_path, index=False)

print(f"Final submission file saved to {output_path}")
