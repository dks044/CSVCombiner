import pandas as pd

# 파일 불러오기
main_df = pd.read_csv('병합된파일_보험.csv')
merge_df = pd.read_csv('10^1데이터_4.csv')

# '이미지캡션(국문)'과 '이미지캡션(영문)' 열에서 빈 값을 찾아 merge_df의 데이터로 채웁니다.
for column in ['이미지캡션(국문)', '이미지캡션(영문)']:
    # 빈 값을 가진 인덱스 가져오기
    missing_data_indices = main_df[main_df[column].isnull()].index
    
    # 빈 값이 있는 각 인덱스에 대해 merge_df의 값을 사용하여 채우기
    for idx in missing_data_indices:
        if idx < len(merge_df):  # merge_df의 행 수를 넘지 않는지 확인
            main_df.at[idx, column] = merge_df.at[idx, column]

# 수정된 데이터프레임을 새 파일로 저장합니다.
main_df.to_csv('병합된파일_보험_legend2.csv', index=False)
