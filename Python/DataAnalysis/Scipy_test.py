# SciPy

# SciPy의 서브 패키지(서브 모듈)

## scipy.optimize : 최적화
## scipy.stats : 통계
## scipy.interplate : 보간법
## scipy.io : 데이터 입출력
## scipy.linalg : 선형 대수
## scipy.sparse : 희소 행렬
## scipy.special : 특수 수학 함수
## scipy.signal : 신호 처리
## scipy.cluster : 벡터 양자화
## scipy.constants : 물리/수학 상수
## scipy.integrate : 통합
## scipy. ndimage : n차원 이미지 패키지
## scipy.spatial : 공간 데이터 구조 및 알고리즘
## scipy.odr : 직교 거리 회귀
## scipy.fftpack : 푸리에 변환

# 확률 분포 객체를 다루기 위한 명령
## 이산 확률 분포(베르누이 분포, 이항 분포, 다항 분포)
## 연속 확률 분포(정규 분포, 균등 분포...)

# stats 서브 패키지 안에 포함된 명령
## 이산 : bernoulli(베르누이 분포), binom(이항 분포), multinomial(다항 분포)
## 연속 : uniform(균일 분포), norm(가우시안 정규 분포), beta(베타 분포), gamma(감마 분포),
##      t(스튜던트 t분포), chi2(카이제곱 분포), f(F분포), dirichlet(디리클리 분포), multivariate_normal(다변수 가우시안 정규분포)

import scipy as sp
from scipy import stats

rv = sp.stats.norm()         # 정규분포 객체 rv를 생성
print(type(rv))

# 모수 지정
## 확률 분포 객체를 생성할 때는 분포의 형태를 구체적으로 지정하는 모수(parameter)를 인수로 지정해야 한다.
## loc(분포의 기대값), scale(표준편차) 두 개의 모수는 대부분 공통적으로 사용한다.
## size(샘플 생성시 생성될 샘플의 크기), random_state(샘플 생성 시 사용되는 seed값)
rv = sp.stats.norm(loc=1, scale=2)      # 기대값이 1이고 표준편차가 2인 정규분포 객체 생성

# 확률 분포 메서드
## pdf() : 확률 밀도 함수(probability density function)
## pmf() : 확률 질량 함수(probability mass function)
## cdf() : 누적 분포 함수(cumulative distribution function)
## rvs() : 랜덤 샘플 생성(random variable sampling)

# 확률 밀도 함수
import numpy as np
import matplotlib.pylab as plt

x = np.linspace(-6, 6, 100)
pdf = rv.pdf(x)
plt.plot(x, pdf)
plt.grid(True)
plt.show()

# 누적 분포 함수
cdf = rv.cdf(x)
plt.plot(x, cdf)
plt.grid()
plt.show()

# 랜덤 샘플 생성(rvs 메서드를 활용한다. size, random_state 모수를 사용한다.)
rv.rvs(size=(2, 4), random_state=0)
print(rv.rvs(size=(2, 4), random_state=0))

# 실수 분포 plot (seaborn 패키지 : distplot, kdeplot, rugplot)
