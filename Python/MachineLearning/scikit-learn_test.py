# scikit-learn : 파이썬 머신러닝 라이브러리

# 머신러닝의 응용분야
## 분류(Classfication) : 특정 데이터에 레이블을 붙여 분류할 수 있다.
## 클러스터링(Clustring) : 값의 유사성을 기반으로 데이터를 여러 그룹으로 나누는 것
## 추천(Recommendation) : 특정 데이터를 기반으로 다른 데이터를 추천하는 것
## 회기(Regression) ; 과거의 데이터를 기반으로 미래의 데이터를 예측하는 것
## 차원축소 : 데이터의 특성을 유지하면서 데이터의 양을 줄여주는 것

from sklearn import svm

# XOR 연산 활용
xor_data = [
    [0, 0, 0],      # 0과 0이면 0이 나온다는 의미
    [0, 1, 1],      # 0과 1이면 1이 나온다는 의미
    [1, 0, 1],      # 1과 0이면 1이 나온다는 의미
    [1, 1, 0]       # 1과 1이면 0이 나온다는 의미
]

# 주어진 데이터를 분리한다. (학습 데이터와 레이블을 분리)
training_data = []
label = []

for row in xor_data:
    p = row[0]
    q = row[1]
    result = row[2]

    training_data.append([p, q])
    label.append(result)

# SVM 알고리즘을 사용하는 머신러닝 객체 생성
## SVM : 분류, 회귀 알고리즘
### SVC : 분류에 해당하는 알고리즘
### SVR : 회귀에 해당하는 알고리즘
clf = svm.SVC()

# fit() 메서드 : 학습기계에 데이터를 학습시킨다.
clf.fit(training_data, label)

# predic() 메서드 : 학습 데이터를 이용하여 예측한다.
pre = clf.predict(training_data)
print('예측결과 : ',pre)

ok = 0; total = 0

for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok +=1
    total += 1
print('정확도 : ', ok, '/', total, '=', ok/total)
## ok 값과 total 값이 같다면 정확도가 100% 라는 의미

import pandas as pd
import numpy as np
from sklearn import metrics     # support vector machine

# XOR 연산 데이터
inputData = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1],
    [1, 1, 0]
]

xor_df = pd.DataFrame(inputData)

# 학습데이터와 레이블을 분리
trainingData = xor_df.loc[:, 0:1]
label = xor_df.loc[:, 2]

clf = svm.SVC()
clf.fit(trainingData, label)     # 학습시키기
pre = clf.predict(trainingData)         # 예측하기

# 정확도 측정(정답률 확인)
# metrics 모듈에 accuracy_score(), import sklearn import metrics 필요

accuracy = metrics.accuracy_score(label, pre)
print("정확도 : ", accuracy)

# scipy의 sparse 모듈 => 희소 행렬을 구하는 모듈

# numpy에서 특수행렬을 만드는 함수
# eye(N, M=, k=, dtype=) : 항등행렬
## M : 열의 수
## k : 대각의 위치
print(np.eye(4, M=3, k=1, dtype=int))

# diag() 함수는 정방행렬에서 대각 요소만 추출하여 벡터를 만든다.
# diag(v, k=, )
## k : 시작 위치
x = np.eye(5, dtype=int)
print(np.diag(x))

x = np.arange(9).reshape(3, 3)
print(x)
print(np.diag(x))
print(np.diag(np.diag(x)))      # diag()함수는 반대로 벡터 요소를 대각 요소로 하는 정방 행렬을 만들 수 있다.


# scipy에서 scikit-learn 알고리즘을 구현할 때 가장 중요한 기능은 scipy.sparse 모듈
# 이때 희소 행렬기능은 주요 기능 중의 하나이다.
# 희소 행렬(sparse matrix) : 0을 많이 포함한 2차원 배열

from scipy import sparse

b1 = np.eye(4, dtype=int)

print("Numpy 배열 : \n{}".format(b1))

# sparse.csr_matrix() : 0이 아닌 원소만 저장
# CSR(Compressed Sparse Row) : 행의 인덱스를 압축해서 저장

sparse_matrix = sparse.csr_matrix(b1)
print("Scipy의 CSR 행렬 : \n{}".format(sparse_matrix))

b2 = np.eye(5, k=-1, dtype=int)
print(b2)

sparse_matrix = sparse.csr_matrix(b2)
print("Scipy의 CSR 행렬2 : \n{}".format(sparse_matrix))

b3 = np.arange(16).reshape(4, 4)
print(b3)

x = np.diag(b3)
print(x)

y = np.diag(np.diag(b3))
print(y)

sparse_matrix = sparse.csr_matrix(y)
print("SciPy의 CSR 행렬3 : \n{}".format(sparse_matrix))

# 희소행렬을 직접 만들 때 사용하는 format
## COO 포맷(Coordinate 포맷), 메모리 사용량을 많이 줄여준다.

data = np.ones(4)
print(data)

row_indices = np.arange(4)
col_indices = np.arange(4)

eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO 표현 : \n{}".format(eye_coo))
# 이러한 예제로는 데이터 양이 적기 때문에 체감하지 못하지만 빅데이터를 다룰 때 메모리양이 부족해서 오류가 나는 경우를 방지해 준다.


# 내장 데이터셋 불러오기
from sklearn.datasets import load_iris

irisData = load_iris()      # Bunch 클래스 객체라고 한다. Python의 딕셔너리 객체 형태와 유사하다.
print(irisData.keys())

print(irisData['target_names'])

print(irisData['data'].shape)

# 데이터를 훈련용 data와 테스트용 data로 나누는 과정이 필요하다.
# 보통 7:3 혹은 8:2 비율로 나눠준다.
# train_test_split 로 수행한다.
# train_test_split 모듈은 sklearn.model_selection에 존재한다.
# train_test_split 수행하기 전 데이터의 섞는 과정이 필요하다.
# scikit-learn 에서 데이터는 보통 대문자 X로 표기하고 label은 소문자 y로 표현한다.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(irisData['data'], irisData['target'], random_state=0)

# train_test_split()의 리턴 타입은 모두 numpy 배열이다.
print(X_train.shape)

print(X_test.shape)

print(y_train.shape)

print(y_test.shape)


# KNN : K-Nearest Neighbors => K-최근접 이웃 알고리즘
## 사용하기 쉬운 분류 알고리즘(분류기) 중의 하나이다.
## 새로운 데이터를 훈련 데이터 중 가장 가까운 데이터를 찾아내는 것
## k의 의미는 가장 가까운 이웃 하나를 의미하는 것이 아니라 훈련데이터에서 새로운 데이터에 가장 가까운 k개의 이웃을 찾는다는 의미

# KNN을 사용하기 위해서는 neighbors 모듈의 KNeighborsClassifier 함수 사용
# KNeighborsClassifier() 함수의 중요한 매개변수는 n_neighbors
# 이 매개변수는 이웃의 개수를 지정하는 매개변수

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)

# 훈련 데이터셋을 가지고 모델을 만들려면 fit 메서드를 사용한다
# fit 메서드의 리턴값은 knn객체를 리턴한다.

knn.fit(X_train, y_train)
print(knn.fit(X_train, y_train))

# 채집한 붓꽃의 새로운 데이터(샘플)라고 가정하고 Numpy 배열로 특성값을 만든다.
# scikit-learn에서는 항상 데이터가 2차원 배열일 것으로 예측해야 한다.

X_newData = np.array([[5.1, 2.9, 1, 0.3]])

# knn 객체의 predict() 메서드를 사용하여 예측할 수 있다.
prediction = knn.predict(X_newData)
print('예측 : ', prediction)

print('예측한 품종의 이름 : ', irisData['target_names'][prediction])

y_predict = knn.predict(X_test)
print(y_predict)

x = np.array([1, 2, 3, 2])

# 정확도를 계산하기 위해 numpy의 mean() 메서드 사용
# knn객체의 score() 메서드를 사용해도 된다.
print(np.mean(y_predict == y_test))     # 1에 가까울수록 정확도가 높다는 의미 
## 이 의미는 y_predict가 X_test에 대한 예측값과의 비교
print(knn.score(X_test, y_test))



