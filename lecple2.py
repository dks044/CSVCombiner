import chardet

# 파일 경로
file_path = '메타데이터_100%_복사본.csv'

# 파일의 인코딩 확인
with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())

# 인코딩 형식 출력
print(result['encoding'])
