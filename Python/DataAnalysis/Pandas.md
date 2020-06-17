# Pandas 

- 데이터 분석 기능을 제공하는 라이브러리.
- 예를 들면, CSV파일 등의 데이터를 읽고 원하는 데이터 형식으로 변환



### pandas 자료구조

#### Series

- Series는 일차원 배열 같은 자료구조

```python
import pandas as pd
from pandas import Series, DataFrame

obj = Series([3, 22, 34, 11])
print(obj)
#0     3
#1    22
#2    34
#3    11
#dtype: int64

# enumerate() 함수를 쓴 것 처럼 1차원 배열을 인덱스와 함께 출력해준다.(색인을 보여준다.)
print(obj.values)
# [ 3 22 34 11]
print(obj.index)
# RangeIndex(start=0, stop=4, step=1)

# 인덱스 설정도 가능하다
obj2 = Series([4, 5, 6, 2], index=['c', 'd', 'e', 'f'])
print(obj2)
#c    4
#d    5
#e    6
#f    2
#dtype: int64
print(obj2['c'])
# 4
print(obj2[['d', 'f','c']]) # 여러개의 인덱스를 지정할 때에는 리스트형식으로 불러준다.
#d    5
#f    2
#c    4
#dtype: int64
print(obj2 * 2)     # Series에 연산도 가능하다.
#c     8
#d    10
#e    12
#f     4
#dtype: int64
print('d' in obj2)
#True
```



- Series는 python의 dict 타입을 대신할 수 있다.

```python
data = {
    'kim' : 3400,
    'hong' : 2000,
    'kang' : 1000,
    'lee' : 2400
}

obj3 = Series(data)
print(obj3)     # 단 인덱스의 순서는 key값의 사전 순으로 들어가게 된다.
#kim     3400
#hong    2000
#kang    1000
#lee     2400
#dtype: int64

name = [
    'woo',
    'hong',
    'kang',
    'lee'
]

obj4 = Series(data, index = name)
print(obj4)     # woo 라는 키를 가진 value는 없으므로 NaN
#woo        NaN
#hong    2000.0
#kang    1000.0
#lee     2400.0
#dtype: float64

# 누락된 데이터를 찾을 때 사용하는 함수 : isnull, notnull
print(pd.isnull(obj4))
#woo      True
#hong    False
#kang    False
#lee     False
#dtype: bool
print(pd.notnull(obj4))
#woo     False
#hong     True
#kang     True
#lee      True
#dtype: bool
```



- Series의 index 값을 바꾸려 할 때

```python
data = {
    'Seoul' : 4000,
    'Busan' : 2000,
    'Incheon' : 1500,
    'Kwangju' : 1000
}
obj5 = Series(data)
print(obj5)
#Seoul      4000
#Busan      2000
#Incheon    1500
#Kwangju    1000
#dtype: int64

# 인덱스만 바꾸려고 할 때
cities = ['Seoul', 'Daegu', 'Incheon', 'Kwangju']
obj6 = Series(data, index=cities)
print(obj6)
#Seoul      4000.0
#Daegu         NaN
#Incheon    1500.0
#Kwangju    1000.0
#dtype: float64
```



- Series끼리의 덧셈은 서로 둘 다 존재하는 데이터끼리 더하여 출력해 준다.
  - NaN값과 일반 값을 더하면 NaN이 된다.

```python
print(obj5 + obj6)
#Busan         NaN
#Daegu         NaN
#Incheon    3000.0
#Kwangju    2000.0
#Seoul      8000.0
#dtype: float64
```



- Series객체와 Series의 색인(index)은 name이라는 속성이 존재한다.

```python
obj6.name = '인구수'        # Series 객체의 이름
print(obj6)
#Seoul      4000.0
#Daegu         NaN
#Incheon    1500.0
#Kwangju    1000.0
#Name: 인구수, dtype: float64

obj6.index.name = '도시'
print(obj6)
#도시
#Seoul      4000.0
#Daegu         NaN
#Incheon    1500.0
#Kwangju    1000.0
#Name: 인구수, dtype: float64
```



- index 이름 변경도 가능하다.

```python
obj6.index = ['Daejeon', 'Busan', 'jaeju', 'jeonju']
print(obj6)
#Daejeon    4000.0
#Busan         NaN
#jaeju      1500.0
#jeonju     1000.0
#Name: 인구수, dtype: float64
```



#### DataFrame

- DataFrame은 2차원리스트(2차원 배열) 같은 자료구조
- R언의 data.frame과 비슷하다.

```python
import pandas as pd
a = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a)
#   0  1  2
#0  1  2  3
#1  4  5  6
#2  7  8  9
```



- dic(딕셔너리)형태의 데이터타입을 통해서도 dataframe 타입을 만들 수 있다.

```python
data = {
    'city' : ['서울', '부산', '광주', '대구'],
    'year' : [2000, 2001, 2002, 2001],
    'pop' : [4000, 2000, 1000, 1000]
}
df = pd.DataFrame(data)
print(df)
#  city  year   pop
#0   서울  2000  4000
#1   부산  2001  2000
#2   광주  2002  1000
#3   대구  2001  1000
```



- 컬럼 순서를 원하는대로 지정할 수 있다.

```python
df = DataFrame(data, columns = ['year', 'city', 'pop'])
print(df)
#   year city   pop
#0  2000   서울  4000
#1  2001   부산  2000
#2  2002   광주  1000
#3  2001   대구  1000
```



- 존재하지 않는 값은 NaN이 출력된다.
- index 지정을 통해 원하는 index 설정도 가능하다.

```python
df2 = pd.DataFrame(data, columns=['year', 'city', 'pop', 'debt'], index=['one', 'two', 'three', 'four'])
print(df2)  
#       year city   pop debt
#one    2000   서울  4000  NaN
#two    2001   부산  2000  NaN
#three  2002   광주  1000  NaN
#four   2001   대구  1000  NaN
```



- 원하는 컬럼 내용만 따로 확인이 가능하다.

```python
print(df2['city'])
#one      서울
#two      부산
#three    광주
#four     대구
#Name: city, dtype: object
```



- 컬럼값만 가져오는 방법

```python
print(df2.columns)
#Index(['year', 'city', 'pop', 'debt'], dtype='object')
```



- 행 전체 값을 가져오는 방법 (기존에 ix 메서드 였으나 최근 없어지고 loc와 iloc가 기능을 대체)
  - row(행)의 위치를 접근할 때 사용하는 메서드(index 값을 통해 검색)
  - 색인을 name속성의 값으로 할당한다.

```python
print(df2.loc['one'])
#year    2000
#city      서울
#pop     4000
#debt     NaN
#Name: one, dtype: object
```



- dataframe에 값을 넣는 방법

```python
df2['debt'] = 1000
print(df2)
#       year city   pop  debt
#one    2000   서울  4000  1000
#two    2001   부산  2000  1000
#three  2002   광주  1000  1000
#four   2001   대구  1000  1000

df2['debt'] = np.arange(4.)
print(df2)
#       year city   pop  debt
#one    2000   서울  4000   0.0
#two    2001   부산  2000   1.0
#three  2002   광주  1000   2.0
#four   2001   대구  1000   3.0

 # Series 객체는 index가 붙는 데이터형식이므로 그냥 넣으면 dataframe과 매칭이 안되어 오류가 난다.
val = Series([1000, 2000, 3000, 4000], index=['one', 'two', 'three', 'four'])     
df2['debt'] = val
print(df2)
#       year city   pop  debt
#one    2000   서울  4000  1000
#two    2001   부산  2000  2000
#three  2002   광주  1000  3000
#four   2001   대구  1000  4000

# 이런식으로 인덱스를 지정하지 않고 넣을 수 있는데 지정하지 않은 인덱스의 해당 값은 NaN값이 뜬다.
val1 = Series([1000, 3000, 5000], index=['one', 'three', 'four'])
df2['debt'] = val1      
print(df2)
#       year city   pop    debt
#one    2000   서울  4000  1000.0
#two    2001   부산  2000     NaN
#three  2002   광주  1000  3000.0
#four   2001   대구  1000  5000.0

df2['aaa'] = df2.city =='서울'
print(df2)
#       year city   pop    debt    aaa
#one    2000   서울  4000  1000.0   True
#two    2001   부산  2000     NaN  False
#three  2002   광주  1000  3000.0  False
#four   2001   대구  1000  5000.0  False
```



- 컬럼 지우는 방법

```python
del df2['aaa']
print(df2)
#       year city   pop    debt
#one    2000   서울  4000  1000.0
#two    2001   부산  2000     NaN
#three  2002   광주  1000  3000.0
#four   2001   대구  1000  5000.0
```



- 딕셔너리 형식 안에 또 하나의 딕셔너리가 존재하는 경우의 dataframe

```python
data2 = {
    'seoul' : {2001 : 20, 2002 : 30},
    'busan' : {2000 : 10, 2001 : 200, 2002 : 300}
}

df3 = pd.DataFrame(data2)
print(df3)
#      seoul  busan
#2001   20.0    200
#2002   30.0    300
#2000    NaN     10

# 메인 딕셔너리의 key값은 컬럼명으로, 내부 딕셔너리 객체의 key값은 index로 나타난다.
```

- 위의 컬럼과 row 값을 바꾸고 싶다면 T를 추가하면 된다.

``` PYTHON
print(df3.T)
#        2001   2002  2000
#seoul   20.0   30.0   NaN
#busan  200.0  300.0  10.0
```

- 데이터프레임에서 values 속성은 저장된 데이터를 2차원 배열로 리턴한다.

``` python
print(df3.values)
#[[ 20. 200.]
# [ 30. 300.]
# [ nan  10.]]
```



#### 색인

- 색인(index) 객체
  - pandas의 색인 객체는 표형식의 데이터에서 각 행과 열에 대한 헤더(이름)와 다른 메타데이터(축의 이름)를 저장하는 객체
  - Series나 DataFrame 객체를 생성할 때 사용되는 배열이나 순차적인 이름은 내부적으로 색인으로 변환된다.

``` python
obj = Series(range(3), index=['a', 'b', 'c'])
print(obj)
#a    0
#b    1
#c    2
#dtype: int64

idx = obj.index

print(idx)
# Index(['a', 'b', 'c'], dtype='object')
print(idx[1])
# b
print(idx[1:])
# Index(['b', 'c'], dtype='object')
```



- 색인 객체는 변경할 수 없다
  - `idx[1] = 'd'` : 에러가 뜬다

``` python
index2 = pd.Index(np.arange(3))
print(index2)
# Int64Index([0, 1, 2], dtype='int64')
```



- 재색인(reindex) : 새로운 색인에 맞도록 객체를 새로 생성하는 기능
  - 객체가 없는 값은 NaN값으로 대체하며 index 자체를 바꾸는 것이 아닌 출력 순서가 바뀌는 것이다.

``` python
obj = Series([2.3, 4.3, -4.1, 3.5], index=['d', 'b', 'a', 'c'])
print(obj)
#d    2.3
#b    4.3
#a   -4.1
#c    3.5
#dtype: float64

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)
#a   -4.1
#b    4.3
#c    3.5
#d    2.3
#e    NaN
#dtype: float64
```



- NaN값 대신 어떠한 값으로 채우고 싶다면 fill_value 속성을 이용한다.

``` python
obj3 = obj.reindex(['a', 'b', 'c', 'c', 'e', 'f'], fill_value=0.0)
print(obj3)
#a   -4.1
#b    4.3
#c    3.5
#c    3.5
#e    0.0
#f    0.0
#dtype: float64
```



- 종합 활용

``` python
df = DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'], columns=['x', 'y', 'z'])
print(df)
#   x  y  z
#a  0  1  2
#b  3  4  5
#c  6  7  8

df2 = df.reindex(['a', 'b', 'c', 'd'])
print(df2)
#     x    y    z
#a  0.0  1.0  2.0
#b  3.0  4.0  5.0
#c  6.0  7.0  8.0
#d  NaN  NaN  NaN

col = ['x', 'w', 'z']
print(df.reindex(columns = col))
#   x   w  z
#a  0 NaN  2
#b  3 NaN  5
#c  6 NaN  8
```



- mehtod 속성의 ffill을 활용해 앞의 값으로 채우는 방법도 있다.

```python
obj4 = Series(['blue', 'red', 'yellow'], index=[0, 2, 4])
print(obj4)
#0      blue
#2       red
#4    yellow
#dtype: object

obj5 = obj4.reindex(range(6), method='ffill')
print(obj5)
#0      blue
#1      blue
#2       red
#3       red
#4    yellow
#5    yellow
#dtype: object
```



- DataFrame 에서의 ffill
  - 데이터프레임에서 보간은 row(행)에 대해서만 이루어진다. 

``` python
df = DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'd'], columns=['x', 'y', 'z'])
col = ['x', 'y', 'w', 'z']
df3 = df.reindex(index=['a','b', 'c', 'd'], method = 'ffill', columns= col)
print(df3)
#   x  y   w  z
#a  0  1 NaN  2
#b  3  4 NaN  5
#c  3  4 NaN  5
#d  6  7 NaN  8
# 컬럼값은 NaN으로 채워지지 않으나 row값은 앞의 값으로 채워졌다.
```



#### 삭제

- Series 삭제
  - 여러개의 값을 지울 때에는 list형식으로 준다.

``` python
obj = Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
#a    0
#b    1
#c    2
#d    3
#e    4
#dtype: int32
    
obj2 = obj.drop('c')
print(obj2)
#a    0
#b    1
#d    3
#e    4
#dtype: int32

obj3 = obj.drop(['b', 'd', 'c'])
print(obj3)
#a    0
#e    4
#dtype: int32
```



- DataFrame 삭제
  - 컬럼을 지울때에는 axis 값을 1로 준다.

``` python
df = DataFrame(np.arange(16).reshape(4, 4), index = ['seoul', 'busan', 'daegu', 'incheon'], columns=['one', 'two', 'three', 'four'])
print(df)
#         one  two  three  four
#seoul      0    1      2     3
#busan      4    5      6     7
#daegu      8    9     10    11
#incheon   12   13     14    15

# 행을 지울때
new_df = df.drop(['seoul', 'busan'])
print(new_df)
#         one  two  three  four
#daegu      8    9     10    11
#incheon   12   13     14    15

# 컬럼을 지울때 => axis 값을 1로 준다.
new_df = df.drop(['one', 'three'], axis=1)
print(new_df)
#         two  four
#seoul      1     3
#busan      5     7
#daegu      9    11
#incheon   13    15
```



#### Series 슬라이싱

``` python
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj['b':'d'])
#b    1.0
#c    2.0
#d    3.0
#dtype: float64
```

- 슬라이싱을 통한 값 변경

``` python
obj['b' : 'c'] = 10
print(obj)
#a     0.0
#b    10.0
#c    10.0
#d     3.0
#dtype: float64
```



#### DataFrame 슬라이싱

``` python
data = DataFrame(np.arange(16).reshape(4, 4), index = ['seoul', 'busan', 'kwangju', 'daegu'],
columns = ['one', 'two', 'three', 'four'])
print(data)
#         one  two  three  four
#seoul      0    1      2     3
#busan      4    5      6     7
#kwangju    8    9     10    11
#daegu     12   13     14    15

print(data['two'])
#seoul       1
#busan       5
#kwangju     9
#daegu      13
#Name: two, dtype: int32

print(data[['one' , 'three']])
#         one  three
#seoul      0      2
#busan      4      6
#kwangju    8     10
#daegu     12     14

print(data[:2])
#       one  two  three  four
#seoul    0    1      2     3
#busan    4    5      6     7

print(data[2:])
#         one  two  three  four
#kwangju    8    9     10    11
#daegu     12   13     14    15

print(data[data['three'] > 7])
#         one  two  three  four
#kwangju    8    9     10    11
#daegu     12   13     14    15

print(data < 5)
#           one    two  three   four
#seoul     True   True   True   True
#busan     True  False  False  False
#kwangju  False  False  False  False
#daegu    False  False  False  False

data[data < 5] = 0
print(data)
#         one  two  three  four
#seoul      0    0      0     0
#busan      0    5      6     7
#kwangju    8    9     10    11
#daegu     12   13     14    15
```

- loc 활용

``` python
print(data.loc['seoul'])
#one      0
#two      0
#three    0
#four     0
#Name: seoul, dtype: int32

print(data.loc['busan', ['two', 'three']])
#two      5
#three    6
#Name: busan, dtype: int32
```

- loc를 활용하면 순서를 마음대로 지정이 가능하다

``` python
print(data.loc[['daegu', 'kwangju'], ['three', 'two']])
#         three  two
#daegu       14   13
#kwangju     10    9
```



### pandas 연산

#### 색인이 다른 객체를 더하는 산술연산

- Series나 DataFrame나 같이 겹쳐있는 값이 있다면 연산하고 그 외에는 NaN과 연산하면 NaN이 되는 법칙에 의해 NaN이 된다.

``` python
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

s1 = Series([5, 6, -1, 2], index=['a', 'c', 'd', 'e'])
s2 = Series([3, 4, -1, 2, 7], index=['a', 'c', 'e', 'f', 'g'])

print(s1 + s2)
#a     8.0
#c    10.0
#d     NaN
#e     1.0
#f     NaN
#g     NaN
#dtype: float64

df1 = DataFrame(np.arange(9).reshape(3, 3), columns=list('bcd'), index=['seoul', 'busan', 'kwangju'])
df2 = DataFrame(np.arange(12).reshape(4, 3), columns=list('bde'), index=['incheon', 'seoul', 'busan', 'suwon'])

print(df1 + df2)
#           b   c     d   e
#busan    9.0 NaN  12.0 NaN
#incheon  NaN NaN   NaN NaN
#kwangju  NaN NaN   NaN NaN
#seoul    3.0 NaN   6.0 NaN
#suwon    NaN NaN   NaN NaN

df3 = DataFrame(np.arange(12).reshape(3, 4), columns=list('abcd'))
df4 = DataFrame(np.arange(20).reshape(4, 5), columns=list('abcde'))
print(df3 + df4)
#      a     b     c     d   e
#0   0.0   2.0   4.0   6.0 NaN
#1   9.0  11.0  13.0  15.0 NaN
#2  18.0  20.0  22.0  24.0 NaN
#3   NaN   NaN   NaN   NaN NaN

print(df3.add(df4, fill_value=0))
#      a     b     c     d     e
#0   0.0   2.0   4.0   6.0   4.0
#1   9.0  11.0  13.0  15.0   9.0
#2  18.0  20.0  22.0  24.0  14.0
#3  15.0  16.0  17.0  18.0  19.0
```

- fill_value 속성은 NaN값은 0으로 채우겠다는 의미

  결론적으로 df4의 값과 0이 더해진 값이 된다.



- DataFrame과 Series와의 연산은 Numpy의 브로드캐스팅과 유사하다.

```python
print(df3.reindex(columns = df4.columns, fill_value = 0))
#   a  b   c   d  e
#0  0  1   2   3  0
#1  4  5   6   7  0
#2  8  9  10  11  0

arr = np.arange(12,).reshape(3, 4)
print(arr)
#[[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]

print(arr[0])
# [0 1 2 3]

print(arr -arr[0])
#[[0 0 0 0]
# [4 4 4 4]
# [8 8 8 8]]


#0 1 2 3    -    0 1 2 3
#4 5 6 7
#8 9 10 11
```

- DataFrame과 Series의 연산

``` python
df = DataFrame(np.arange(12).reshape(4, 3), columns=list('bde'), index=['seoul', 'kwangju', 'daegu', 'incheon'])
print(df)
#         b   d   e
#seoul    0   1   2
#kwangju  3   4   5
#daegu    6   7   8
#incheon  9  10  11

s1 = df.iloc[0]
print(s1)
#b    0
#d    1
#e    2
#Name: seoul, dtype: int32

print(df-s1)
#         b  d  e
#seoul    0  0  0
#kwangju  3  3  3
#daegu    6  6  6
#incheon  9  9  9

# s1의 0, 1, 2의 값이 df의 b d e에 모두 계산된다.

s2 = Series(range(3), index=list('bef'))
print(s2)
#b    0
#e    1
#f    2
#dtype: int64

print(df + s2)
#           b   d     e   f
#seoul    0.0 NaN   3.0 NaN
#kwangju  3.0 NaN   6.0 NaN
#daegu    6.0 NaN   9.0 NaN
#incheon  9.0 NaN  12.0 NaN

s3 = df['d']
print(s3)
#seoul       1
#kwangju     4
#daegu       7
#incheon    10
#Name: d, dtype: int32

print(df + s3)
#          b   d  daegu   e  incheon  kwangju  seoul
#seoul   NaN NaN    NaN NaN      NaN      NaN    NaN
#kwangju NaN NaN    NaN NaN      NaN      NaN    NaN
#daegu   NaN NaN    NaN NaN      NaN      NaN    NaN
#incheon NaN NaN    NaN NaN      NaN      NaN    NaN

# index가 완전히 새롭게 추가되는 경우이기 때문에 모두 NaN값이 뜨는 결과가 나온다.

# 행에 대한 연산을 수행해야 할 경우에는 함수를 이용한다. (add, sub 등) axis값을 주면 된다.
print(df.add(s3, axis=0))
#          b   d   e
#seoul     1   2   3
#kwangju   7   8   9
#daegu    13  14  15
#incheon  19  20  21

print(df.sub(s3, axis=0))
#         b  d  e
#seoul   -1  0  1
#kwangju -1  0  1
#daegu   -1  0  1
#incheon -1  0  1
```



#### 함수 적용과 매핑

- 배열의 각 원소에 적용되는 함수를 유니버셜 함수라 한다.
- numpy.random 모듈에 있는 randn 함수는 임의의 정규분포 데이터를 생성한다.

```python
df = DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['seoul', 'busan', 'daegu', 'incheon'])
print(df)
#                b         d         e
#seoul    0.168250 -0.703088  0.305677
#busan    0.208095 -0.301753  0.303408
#daegu    0.127047 -0.559360  1.138457
#incheon -0.655010 -2.191097 -0.718302

print(np.abs(df))		# abs : 절대값으로 변환하는 함수
#                b         d         e
#seoul    0.168250  0.703088  0.305677
#busan    0.208095  0.301753  0.303408
#daegu    0.127047  0.559360  1.138457
#incheon  0.655010  2.191097  0.718302

f = lambda x : x.max()-x.min()

print(df.apply(f))  # 행 중심으로 계산
#b    0.863105
#d    1.889344
#e    1.856759
#dtype: float64

print(df.apply(f, axis=1))	# 열 중심으로 계산
#seoul      1.008765
#busan      0.605161
#daegu      1.697818
#incheon    1.536087
#dtype: float64
```


