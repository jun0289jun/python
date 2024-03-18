import pandas as pd

# 엑셀 파일 경로 지정
excel_file = 'C:/RPA/example.xlsx'
sheet_name = '2nd Sheet'

# 엑셀 파일의 데이터 읽어오기
data = pd.read_excel(excel_file, sheet_name)

# 데이터 확인
print(data.head())  # 데이터의 상위 몇 개 레코드 출력

df = pd.DataFrame(data)

for index, row in df.iterrows():
    name = row['과일']
    price = row['가격']
    color = row['색']

    print(f"{name}의 가격은 {price}원 이고 색상은 {color}입니다!")