import pandas as pd

# 파일 두개일 때 사용
def ensemble_two_file(file1_path, file2_path):
    # 제출 파일들 읽기
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # 두 개의 예측값 평균 계산 (소프트 보팅)
    df1['prediction'] = (df1['prediction'] + df2['prediction']) / 2

    # 최종 제출 파일 저장
    output_path = 'ensemble_two_submission(soft).csv'
    df1.to_csv(output_path, index=False)

    print(f"Final submission file saved to {output_path}")
    
# 파일 세개일 때 사용
def ensemble_three_file(file1_path, file2_path, file3_path):
    # 제출 파일들 읽기
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)
    df3 = pd.read_csv(file3_path)

    # 세 개의 예측값 평균 계산 (소프트 보팅)
    df1['prediction'] = (df1['prediction'] + df2['prediction'] + df3['prediction']) / 3

    # 최종 제출 파일 저장
    output_path = 'ensemble_three_submission(soft).csv'
    df1.to_csv(output_path, index=False)

    print(f"Final submission file saved to {output_path}")
 
   
file1_path = '.csv'
file2_path = '.csv'
ensemble_two_file(file1_path, file2_path)

