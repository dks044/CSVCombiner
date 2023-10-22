import pandas as pd

# 첫번째 CSV 파일 읽기
df1 = pd.read_csv("메타데이터_100^1_복사본2_제발.csv")
df1['액터번호'] = df1['액터번호'].astype(str).str.zfill(4)

# 두번째 CSV 파일 읽기, '액터번호' 형식 변환
df2 = pd.read_csv("10^1데이터_4.csv")
df2['액터번호'] = df2['액터번호'].astype(str).str.zfill(4)

# 첫 번째 데이터프레임에서 두 번째 데이터프레임의 '액터번호'와 일치하는 행을 업데이트합니다.
for index, row in df2.iterrows():
    df1.loc[df1['액터번호'] == row['액터번호'], ['이미지캡션(국문)', '이미지캡션(영문)']] = row[['이미지캡션(국문)', '이미지캡션(영문)']]

# 결과 CSV 파일로 저장
df1.to_csv("병합된파일.csv", index=False)
