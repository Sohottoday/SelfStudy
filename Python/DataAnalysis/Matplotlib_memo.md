# Matplotlib

- 시각화 패키지

- 데이터를 차트(chart)나 플롯(plot)으로 시각화하는 패키지

  여러 다양한 시각화 기능을 제공한다.

- 라인 플롯(line plot), 스캐터 플롯(scatter plot), 바 차트(bar chart), 히스토그램(histogram) 등

- 서브 패키지

  - pylab

    import matplotlib as mpl

    import matplotlib.pylab as plt 로 불러온다.

``` python
import matplotlib as mpl
import matplotlib.pylab as plt

plt.plot([1, 5, 8, 15])		# plot 명령은 ndarray 객체를 반환한다.
plt.grid(True)
plt.show()
```

![캡처1](https://user-images.githubusercontent.com/58559786/86025333-08314300-ba69-11ea-965e-9ef3557570ec.PNG)

``` python
plt.plot([100, 200, 3030, 400], [1, 4, 10, 17], 'rs--')
plt.show()
```

![캡처2](https://user-images.githubusercontent.com/58559786/86025451-2ac35c00-ba69-11ea-89ad-c0609ee3d2a8.PNG)



- 차트의 스타일 지정 순서 : 색상(color), 마커(marker), 선 종류(line style)

  - `rs--`의 의미는 앞의 r은 색상(red)를 표현한 것이고 s는 점 모양(square),  --는 선 종류를 나타낸 것이다.
  - 선 색상은 r(red), m(magenta), c(cyan) 등 이 존재한다.

  

- Matplotlib가 그리는 그림은 Figure객체, Axes객체, Axis객체로 구성된다.

  Figure 객체는 한개 이상의 Axes객체를 포함할 수 있다.

  Axes객체는 다시 두개 이상의 Axis 객체를 포함한다.

  즉, Axis 객체는 하나의 플롯(plot)을 의미한다.

  Axis는 세로축(y축)이나 가로축(x축) 등의 축을 의미한다.

  

- Figure 객체는 Matplotlib.figure.Figure클래스 객체이다.

  Figure는 플롯에 그려지는 캔버스(도화지)를 뜻한다.



- subplot : 하나의 Figure 안에 여러개의 플롯(plot)을 배열 형태로 보이도록 할 때 사용한다.

  Figure 안에 Axes를 생성하려면 subplot 명령을 사용해서 Axes 객체를 얻어야 한다.

  그러나, plot명령을 사용해도 자동으로 Axes를 생성해 준다.

  subplot(2, 1, 1), subplot(2, 1, 2)

- tight_layout 명령을 실행하면 플롯(Axes)간의 간격을 자동으로 조절해준다.



- np.linspace : Numpy에 존재하는 함수로 (start, stop, num, endpoint=True, retstep=False, dtype)
  - start(시작값)
  - stop(endpoint가 False로 설정되지 않은 경우 끝 값이 된다.)
  - num(생성할 샘플 수, 기본값 50, 음수는 될 수 없다.)
  - endpoint(끝 점), restep(샘플간의 간격을 설정할 수 있는 step을 반환한다)

``` python
print(np.linspace(2.0, 3.0, num=5))
# [2.   2.25 2.5  2.75 3.  ]

print(np.linspace(2.0, 3.0, num=5, endpoint=False))
# [2.  2.2 2.4 2.6 2.8]

print(np.linspace(2.0, 3.0, num=5, retstep=True))
# (array([2.  , 2.25, 2.5 , 2.75, 3.  ]), 0.25)			# 2개의 변수에 따로 담을 수 있다.
```



- 비교해보기
- xlim : x축의 범위를 지정한다.
- ylim : y축의 범위를 지정한다.

``` python
N = 8
y = np.zeros(N)
print(N)
# [0. 0. 0. 0. 0. 0. 0. 0.]

x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)

plt.plot(x1, y, 'o')		# 칼라 없이 마커만 o로 출력된다.
plt.plot(x2, y+0.4, 'o')

plt.ylim([-0.5, 1])		# y축의 값이 -0.5에서 1 사이값으로 축을 지정한다.
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/58559786/86164780-4acc4b80-bb4d-11ea-9cfe-7717591a60b8.png)



``` python
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
plt.plot(X, C)
plt,xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, 1])
plt.grid(True)
plt.show()
```

![Figure_2](https://user-images.githubusercontent.com/58559786/86164977-9979e580-bb4d-11ea-9bf6-5d5137bfbee0.png)

- tick : plot이나 chart에서 축상의 위치 표시 지점을 의미한다.
  - tick에 씌어지는 숫자나 글자를 틱 라벨(tick label)이라 한다.
  - 일반적으로 tick label은 Matplotlib가 자동으로 정해준다.
  - 사용자가 수동으로 설정을 하고싶다면 xticks, yticks 명령을 사용하여 x축과 y축 설정이 가능하다.
  - 틱라벨 문자열을 수학 기호로 표시하고 싶은 경우 $$ 사이에 LaTeXㅅ 수학문자식을 넣어서 사용한다.

``` python
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], ['$-\pi$', '$-\pi/2$', 0, '$\pi/2$', '$\pi$'])
plt.yticks([-1, 0, 1], ['Low', '0', 'High'])
plt.show()
```

![Figure_3](https://user-images.githubusercontent.com/58559786/86165173-e8c01600-bb4d-11ea-8a9b-f62b373192cb.png)



``` python
xx1 = np.linspace(0.0, 5.0)
xx2 = np.linspace(0.0, 2.0)

yy1 = np.cos(2 * np.pi * xx1) * np.exp(-xx1)
yy2 = np.cos(2 * np.pi * xx2)

ax1 = plt.subplot(2, 1, 1)
plt.plot(xx1, yy1, 'ro-')
ax2 = plt.subplot(2, 1, 2)
plt.plot(xx2, yy2, 'b.-')

plt.show()
```

![Figure_4](https://user-images.githubusercontent.com/58559786/86165272-0ab99880-bb4e-11ea-88f6-cbae30d52bcd.png)






