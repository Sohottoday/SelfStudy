import pandas as pd

# Series
pd.Series([1, 2, 3, 4])

a = [1, 2, 3, 4]
print(pd.Series(a))

# DataFrame
company1 = [['삼성', 2000, '스마트폰'],
            ['현대', 1000, '자동차'],
            ['네이버', 500, '포털']]

df1 = pd.DataFrame(company1)
print(df1)
print("-----------")

## 제목 컬럼 만들기
df1.columns = ['기업명', '매출액', '업종']
print(df1)
print("-----------")

## dict로 DataFrame 만들기
company2 = {'기업명' : ['삼성', '현대', '네이버'],
            '매출액' : [2000, 1000, 500],
            '업종' : ['스마트폰', '자동차', '포털']}

df2 = pd.DataFrame(company2)
print(df2)
print("-----------")

## index를 특정 column으로 지정하기
df1.index = df1['기업명']
print(df1)
print("-----------")

# 구글 드라이브에 있는 샘플 파일 읽어오기 (colab에서만 사용 가능)
"""
1. 로컬에서 파일 읽어오기(초심자가 진행하기에는 번거로움)
from google.colab import files
myfile = files.upload()

import io
pd.read_csv(io.BytesIO(myfile['korean-idol.csv']))

2. 구글 드라이브에 있는 샘플 파일 읽어오기
from google.colab import drive
drive.mount('/content/drive')

filename = '이곳에 파일 경로 붙여넣기'
pd.read_csv(filename)

3. 파일 URL로부터 바로 읽어오기
pd.read_csv('http://bit.ly/ds-korean-idol')

"""

# 엑셀 파일 읽어오기
"""
from google.colab import drive
drive.mount('/content/drive')
filename = '파일 경로 붙여넣기'

pd.read_excel(filename)
"""

df = pd.read_csv('korean-idol.csv')
print(df)

# 열 (column) 출력하기
print(df.columns)

# 열 이름 재정의하기
new_col = ['name', '그룹', '소속사', '성별', '생년월일', '키', '혈액형', '브랜드평판지수']
df.columns = new_col

# index(행) 출력하기
print(df.index)

# info는 기본적인 행(row)의 정보와 데이터 타입을 알려준다.
# info 메서드는 주로 빠진 값(null 값)과 데이터 타입을 볼 때 활용한다.
print(df.info())

# 통계 정보 알아보기(describe)
print(df.describe())

# 형태 알아보기(shape)
print(df.shape)

# 오름차순 정렬
print(df.sort_index())

# 내림차순 정렬
print(df.sort_index(ascending=False))

# column 별로 정렬
print(df.sort_values(by='키'))      # 키 컬럼의 순서를 오름차순으로 정렬(by 없이도 가능하다.)
print(df.sort_values('키', ascending=False))

# 복수 정렬
print(df.sort_values(by=['키', '브랜드평판지수']))           # 키가 동일하다면 브랜드 평판 지수로 그 다음 정렬한다.

# column을 선택하는 방법
print(df['name'])
print(df.키)        # 이 방법은 코드의 가독성 때문에 권장하지 않음

# 단순 index에 대한 범위 선택
print(df[:3])

# loc       , 기준으로 왼쪽은 행 오른쪽은 열
print(df.loc[:, 'name'])            
print('--------------------')
print(df.loc[:, ['name', '생년월일']])
print('--------------------')
print(df.loc[3:8, ['name', '생년월일']])
print(df.loc[2:5, 'name':'생년월일'])           # loc는 행을 가져올 때 numpy와는 다르게 2:5 일 경우 5 미만이 아닌 5 이하를 불러온다.

# iloc(position으로 색인)
print(df.iloc[:, [0, 2]])           # 범위를 이름이 아닌 위치로 불러온다.
print(df.iloc[1:5, [0, 2]])         # loc와 다르게 5 미만이라는 의미를 유의하자
print(df.iloc[1:4, 3:6])

# boolean indexing
print(df['키']>180)

print(df[df['키']>180])             # 이 방법은 모든 column을 출력해야 한다는 한계가 있다.

## 해결 방법 1. 맨 뒤에 출력할 column 붙이기
print(df[df['키']>180][['name', '키']])

## 해결 방법 2. loc를 활용
print(df.loc[df['키']>180, 'name':'성별'])
print(df.loc[df['키']>180, ['성별', '혈액형']])

# isin을 활용한 색인
# isin을 활용한 색인은 내가 조건을 걸고자 하는 값이 내가 정의한 list에 있을 때만 색인하려는 경우에 사용
my_condition = ['플레디스', 'SM']
print(df['소속사'].isin(my_condition))
print(df.loc[df['소속사'].isin(my_condition), ['name', '소속사']])

# Null(결측값) 알아보기 = 비어있는 값이라고도 한다.
## pandas에서는 NaN(Not a Number) 이라 표시한다.

# info()로 NaN값, 즉 빠진 데이터가 어디에 있는지 쉽게 요약해 볼 수 있다.
print(df.info())

# NaN값 Boolean 인덱싱 : isna(), isnull()
print(df.isna())            # Boolean 인덱싱으로 True가 return되는 값이 NaN값
print(df['그룹'].isnull())
print('----------------------')
# 위를 활용해 NaN값만 색출해내기
print(df['그룹'][df['그룹'].isnull()])

# NaN이 아닌 값에 대해서 Boolean 인덱싱 : notnull()
# NaN이 아닌 값만 색출
print(df['그룹'][df['그룹'].notnull()])

# loc와 함께 사용하여 인덱싱
print(df.loc[df['그룹'].isnull(), ['키', '혈액형']])

# copy
# new_df = df 이러한 식으로 DataFrame을 복사했을 경우
# new_df['그룹'] = 0   이런 식으로 새로운 값을 넣었을 때 원본 df까지도 변화한다
# 그 이유는 같은 메모리 주소를 참조하기 때문이다.
# 따라서 원본 데이터를 유지하고 새로운 변수에 복사할 때에는 copy()를 사용한다.
new_df = df.copy()
print(hex(id(new_df)), hex(id(df)))




