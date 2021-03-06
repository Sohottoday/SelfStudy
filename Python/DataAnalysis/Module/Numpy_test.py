import numpy as np

list1 = [1, 2, 3, 4]
a = np.array(list1)
print(a)

print(a.shape)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

print(b.shape)

aa = np.zeros((2, 2))	# 2행 3열의 매트릭스를 0으로 다 채운다.
print(aa)
print(type(aa))

aa = np.ones((2, 3))	# 2행 3열의 매트릭스를 1로 다 채운다.
print(aa)

aa = np.full((2, 3), 10)	# 2행 3열의 매트릭스를 10으로 다 채운다.
print(aa)

aa = np.eye(4)		# 4행 4열을 의미하며 대각선에 값을 넣는다.
print(aa)

aa = np.array(range(20)).reshape((5, 4))
print(aa)			# 0부터 19까지 생성한 뒤 5행 4열의 매트릭스에 넣는다.

aa = np.array(range(15)).reshape((3, 5))
print(aa)		# 0부터 15까지 생성한 뒤 3행 5열의 매트릭스에 넣는다.

list2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

arr = np.array(list2)

a = arr[0:2, 0:2]

print(a)

b = arr[1:, 1:]
print(b)

list3 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

a = np.array(list3)

# 정수 인덱싱
res = a[[0, 2], [1, 3]]     # 즉 배열 기준 0행 1열 값과 2행 3열 값을 가져오라는 의미.
print(res)

# boolean 인덱싱

list4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

aa = np.array(list4)

b_arr = np.array([
    [False, True, False],
    [True, False, True],
    [False, True, False]
])      # False는 선택하지 않고 True는 선택하겠다는 의미.

n = aa[b_arr]
print(n)

# 표현식을 통한 boolean indexing 배열 생성
## 배열 aa에 대해서 짝수인 배열 요소만 True로 지정하겠다는 가정
b_arr = (aa % 2==0)
print(b_arr)

print(aa[b_arr])

aaa = aa[aa%2 == 0]
print(aaa)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print(c)

c = np.add(a, b)
print(c)

# 리스트와는 계산 결과 값부터 다르다.
d = [1, 2, 3]
e = [4, 5, 6]
f = d + e
print(f)

c = a - b
print(c)

c = np.subtract(a, b)
print(c)

#c = a * b
c = np.multiply(a, b)
print(c)

#c = a/b
c = np.divide(a, b)
print(c)
print('-----')
# 2차원 배열의 곱 / 매트릭스 배열의 곱
# 1차원 배열을 벡터라 하고 2차원 이상의 배열을 매트릭스라 한다.
list11 = [
    [1, 2],
    [3, 4]
]

list12 = [
    [5, 6],
    [7, 8]
]

a = np.array(list11)
b = np.array(list12)

# numpy에서 vector와 matrix의 product를 구하기 위해서 dot() 함수를 이용한다.
product = np.dot(a, b)
print(product)

s = np.sum(a)
print(s)

s = np.sum(a, axis = 0)
print(s)
s = np.sum(a, axis = 1)
print(s)

p = np.prod(a)
print(p)

p = np.prod(a, axis = 0)
print(p)

p = np.prod(a, axis = 1)
print(p)


x = np.float32(1.0)
print(x)
print(type(x))
print(x.dtype)

z = np.arange(5, dtype='f')    # range 함수와 비슷하지만 나란히 정렬하여 배열을 만든다. 데이터 타입 설정이 가능하다.
print(z)
bb = np.arange(3, 10)
print(bb)
cc = np.arange(3, 10, dtype=np.float)
print(cc)
dd = np.arange(2, 3, 0.1)
print(dd)
print(dd.dtype)

aa = np.array([1, 2, 3], dtype='f')
print(aa.dtype)

xx = np.int8(aa)
print(xx)
print(xx.dtype)


q = np.array([[1, 2], [3, 4]])
w = 10
y = np.array([10, 20])

z = q * w
print(z)

z = q * y
print(z)

qq = np.array([[11, 21], [34, 43], [0, 9]])
print(qq)
print(qq[0][1])

for row in qq:
    print(row)

qq = qq.flatten()
print(qq)

print(qq[np.array([1, 3, 5])])
print(qq[qq>25])    # numpy에 부등호 연산자를 사용할 경우 True False로 값이 나온다.
print(qq > 25)

print(qq.ndim)  
print(qq.itemsize)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)

# 인덱스를 저장할 배열 생성
idx = np.array([0, 2, 0, 1])
print(idx)

print(a[np.arange(4), idx])

print(a[np.arange(4), idx] * 2)

# 벡터의 내적
x = np.array([[1, 2], [3,4]])
v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))     # 또는 np.dot(v, w)
# v[0] * w[0] + v[1] * w[1]

# 매트릭스와 벡터의 곱
print(x.dot(v))
#x[0,0] * v[0] + x[0,1] * v[1] , x[1,0] * v[0] + x[1,1] * v[1]

# 전치 행렬의 표현은 T속성을 이용한다.
tt = np.array([[1, 2], [3, 4]])
print(tt)
print(tt.T)

# 배열 생성 초기화, 값들을 모두 초기화시킨다.
g = np.empty((4, 3))
print(g)

# 3차원 배열 만들기
d = np.array([[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]],
                [[11, 12, 13, 14],
                [15, 16, 17, 18],
                [19, 20, 21, 22]]])

print(d)

# len : 3차원 배열의 행, 열. 깊이 구하는 방법
print(len(d))        # 3차원 배열의 깊이
print(len(d[0]))     # 3차원 배열의 행
print(len(d[0][0]))  # 3차원 배열의 열

c = np.ones((2, 3, 4), dtype="i")
print(c)

# ones_like() : 지정한 배열과 똑같은 크기의 배열을 만든다
# (copy와 다른점은 dtype의 설정이 가능하므로 같은 크기의 다른 종류의 배열을 만들 수 있다.)
k = np.ones_like(c)

cc = np.copy(c)


# 차원 축소 연산(dimension reduction 연산)
## 행렬의 하나의 행에 있는 원소들을 하나의 데이터 집합으로 보고 그 집합의 평균을 구하면
##각 행에 대해 하나의 숫자가 나오게 되는데 이 경우 차원 축소가 된다. 이러한 연산을 차원 축소 연산이라 한다.

# Numpy에서의 차원 축소 연산 명령 또는 메서드
# 최대/최소 : min, max, argmin, argmax
# 통계 : sum, mean, median, std, var
# boolean : all, any

x = np.array([1,10, 100])
print(x)
print(x.min())

# argmin : 최소값의 위치
# argmax : 최대값의 위치
print(x.argmin())
print(x.argmax())

# mean : 평균값
# median : 중간값, 여러개의 숫자들이 있을 때 크기순으로 정렬한 다음 가장 가운데 위치한 숫자
# 개수가 짝수개일 경우 중간의 좌우값의 평균값을 반환한다.
# std : 
# var : 
print(x.mean())
print(np.median(x))

# all : 모든 조건이 들어 맞을때
# any : 하나의 조건이라도 들어 맞을때

print(np.all([True, True, False]))
print(np.any([False, False, True, False]))

# axis 속성을 부여하는 메서드들은 대부분 차원 축소 명령에 속한다.

# 정렬
# sort명령이나 메서드를 사용하여 배열안의 원소를 크기에 따라 정렬하여 새로운 배열을 만들 수 있다.
# 2차원 이상인 경우에는 행이나 열을 각각 따로 정렬할 수 있는데 이때, axis 속성을 사용하여 행과 열을 결정할 수 있다.

a = np.array([[4, 3, 5, 7],
            [1, 12, 11, 9],
            [2, 15, 1, 14]
            ])
print(np.sort(a))   # default값이 1이다
print(np.sort(a, axis=0))
print(a.argsort())  # 자료를 정렬하는 것이 아닌 순서만 알고싶을 때 사용된다.

# 배열 더하기(합성)
a = np.array([1, 2, 3])
b = np.array([3, 2, 3])
# column_stack() 배열을 열 기준으로 합침, 3개 이상도 사용 가능하다.
print(np.column_stack((a, b)))

# 배열 나누기(쪼개기)
# split = array_split

x = np.arange(9.0)
print(x)

x_1 = np.split(x, 3)
# x_1 = np.array_split(x, 3)
print(x_1)

print(x_1[1])

x2 = np.split(x, [3, 4])    # 인덱스 3위치에서 한번 나누고 4위치에서 한번 나누겠다는 의미
# 이런식으로 자신이 원하는대로 자를 수 있다.
print(x2)

# dsplit : 3차원 배열 나누기
y = np.arange(16).reshape(2, 2, 4)
print(y)

print(np.dsplit(y, 2))
print('------------')

# hsplit : 3차원 배열 열 기준으로 나누기
print(np.hsplit(y, 2))
print("----------")

# vsplit: 수직 기준으로 3차원 배열 나누기
print(np.vsplit(y, 2))

# 반복 생성
a = np.array([0, 1, 2])
print(np.tile(a, 2))
print(np.tile(a, (2, 2)))

b = np.array([[1, 2], [3, 4]])
print(np.tile(b, 2))
print(np.tile(b, (2,2)))

# 배열 반복
print(np.repeat(3, 4))  # 3을 4번 반복하는 배열 생성
x = np.array([[1, 2], [3, 4]])
print(np.repeat(x, 2))

print(np.repeat(x, 3, axis=0))

# 배열 요소에 대한 추가 및 삭제
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 11, 12, 13]])
print(arr)

# delete
print(np.delete(arr, 1))
print(np.delete(arr, 1, 0)) # axis값을 줘야 배열의 요소 하나가 아닌 행전체 혹은 열 전체의 삭제가 가능하다.
print(np.delete(arr, 2, 1))

# insert
print(np.insert(arr, 1, 100))
print(np.insert(arr, 1, 100, axis = 1)) # delete와 같은 맥락으로 axis값이 주어져야 한다.
print(np.insert(arr, 1, 100, 0))
print(np.insert(arr, 1, [100, 200, 300], axis=1))

# append
print(np.append(arr, [[100, 101, 102, 103]], axis=0))      # 정확하게 2차원 배열에 추가할 때에는 2차원 형식으로 추가해줘야 한다

# resize
print(np.resize(arr, (3, 5)))       # resize를 통해 사이즈를 크게 만들면 다시 첫 값부터 들어가게 된다.
print(np.resize(arr, (2, 3)))       # resize를 통해 사이즈를 작게 만들면 뒤의 값부터 없어진다.

# trim_zeros : 좌우의 0을 제거
aa = np.array((0, 0, 0, 1, 2, 3, 0, 1, 2, 0, 0))
print(np.trim_zeros(aa))
print(np.trim_zeros(aa, 'f'))       # 속성으로 f를 주면 앞부분의 0만 제거되고 b를 주면 뒷부분의 0만 제거된다.

# unique : 중복된 값을 하나로 만들어준다.
a = np.array([1, 1, 2, 1, 2, 2, 3, 3, 3])
print(np.unique(a))

aa = np.array([[1, 1, 3, 2], [2, 3, 3, 1]])
print(np.unique(aa))

a = np.array([[1, 0, 0], [1, 0, 0], [2, 3, 4]])
print(np.unique(a, axis=0))     # 중복된 행 자체를 병합시킨다.

# 요소의 재정렬
# flip : 뒤집어 엎다.

b = np.arange(8).reshape((2, 2, 2))
print(b)
print(np.flip(b, 0))
print(np.flip(b, 1))
print(np.flip(b))       # axis 값을 주지 않으면 완전히 뒤집어진다.

# diag() : 대각선 값 추출
x = np.arange(9).reshape((3, 3))
print(np.diag(x))
print(np.diag(x, k=1))  # k값 설정을 통해 몇번째 대각선을 출력할건지 선택이 가능하다.
print(np.diag(x, k=-1)) 

# diag()를 활용한 배열 생성
c = np.diag([1, 2, 3])
print(c)

# fliplr : 왼쪽 / 오른쪽 방향으로 뒤집기
print(np.fliplr(c))


# flipud : 배열을 위/아래 방향으로 뒤집기
print(np.flipud(c))

# rot90 : 배열을 90도만큼 회전시킴
## k : 몇번 움직일것인지를 선택하는 속성
## axes : 회전 축 설정(0, 1) 또는 (1, 0)  ,0에서 1방향으로 축 설정

m = np.array([[1, 2], [3, 4]])
print(m)

print(np.rot90(m, k=1))

print(np.rot90(m, k=1, axes=(1,0)))

print(np.rot90(m, k=1, axes=(0,1)))



# Numpy 기술 통계(descriptive statistics)
# len() : 데이터의 개수(count) => np.mean(x)
# mean() : 평균(average, mean)  / 통계 용어로는 샘플 평균이라 함 => np.mean(x)
# var() : 분산(variance) / 통계 용어로 샘플 분산 => np.var(x)
# std() : 표준편차(standard deviation) / 수학 기호로는 s 라고 표현된다 => np.std(x)
# max() : 최대값(maximum) => np.max(x)
# min() : 최소값(minimum) => np.min(x)
# median() : 중앙값(median) => np.median(x)
# percentile() : 사분위수(quartile)
## np.percentile(x, 0) : 최소값
## np.percentile(x, 24) : 1사분위수
## np.percentile(x, 50) : 2사분위수
## np.percentile(x, 75) : 3사분위수
## np.percentile(x, 100) : 최대값


# 난수(random) 발생
# rand() : 0과 1 사이의 숫자를 무작위 추출
print(np.random.rand())

# seed(씨앗값) 설정 : 겉보기에는 무작위 수처럼 보이지만 실제로는 컴퓨터가 처음 만들어질 때 생성된 셋팅값에 의해 일정한 값이 추출된다.
np.random.seed(0)
print(np.random.rand(5))
print(np.random.rand(7))

np.random.seed(0)
print(np.random.rand(5))

# 데이터의 순서 바꾸기
# shuffle : 데이터를 섞음

x = np.arange(10)
print(x)
np.random.shuffle(x)
print(x)
# shuffle은 배열 자체를 섞는것이기 때문에 print(np.random.shuffle(x))는 None값이 리턴된다.

# 데이터 샘플링 : 이미 있는 데이터 집합에서 무작위로 선택하는 것
# choice : np.random.choice(a, size, replace, p)
## a : 원본 데이터, 정수이면 range(a)
## size : 샘플 숫자
## replace : True : 한번 선택한 데이터를 다시 선택할 수 있다. / False : 한번 선택한 데이터는 다시 선택할 수 없다.
## p : 배열, 각 데이터가 선택될 수 있는 확률

x = np.random.choice(5, 5, replace=True)
print(x)

x1 = np.random.choice(10, 3, replace=False)
print(x1)

x2 = np.random.choice(5, 10, p=[0.2, 0, 0, 0.3, 0.5])
print(x2)

# randn() : 가우시안 표준 정규 분포
print(np.random.randn(5))

# randint(low, high, size) : 균일 분포의 정수 난수
## high 값이 없으면 low와 0 사이의 숫자, high 값이 있으면 low~high 사이의 숫자를 출력한다. size는 난수의 개수를 의미
print(np.random.randint(10, size=10))
print(np.random.randint(1, 45, size=7))


# 정수 데이터 카운팅
# unique : 데이터에서 중복된 값을 제거하고 중복되지 않는 값의 리스트를 출력
## return_counts 속성 : True - 데이터의 갯수도 출력
a = np.unique([1, 1, 2, 2, 2, 3, 3, 3, 3], return_counts=True)
print(a)

b = np.array(['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c'])
data, counts = np.unique(b, return_counts=True)     # 이런식으로 변수를 따로 넣으면 각각 넣을 수 있다.
print(data)
print(counts)


# bincount : minlength 인수를 설정하여 사용하면 편리하다.
## unique는 실제로 나온 숫자만 카운트하므로 나올 수 있는 수자에 대한 카운트는 하지 않는다.
## 하지만 bincount는 나올 수 있는 숫자의 카운트를 0으로 한다.

print(np.bincount([1, 1, 2, 2, 3, 4], minlength=6))
