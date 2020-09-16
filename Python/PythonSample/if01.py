
# 축구 경기에서 이기면 승점 3점 취득
# 정답이 맞으면 1점을 추가
# 해당 파일이 존재하지 않으면 오류 메세지 출력

# 제어문 = 조건문 + 반복문 + etc
# 조건문 : 만약 ~~~ 하면  ~~~ 하시오 . if구문
# 반복문 : 특정한 구문이나 패턴을 반복적으로 수행해주는 구문. for 구문

# if
'''
if 조건문:
    참일 때 수행
else:
    거짓일 때 수행
'''
# 어떤 수가 짝수인지 홀수인지 판단하기
# 양자 택일 구문(둘 중 하나)
su1 = 8
if su1 % 2 == 0:
    print('짝수')
else:
    print('홀수')

print('-' * 30)

# 짝수일때만 출력하기
# 단순 if 구문
su1 = 8
if su1 % 2 == 0:
    print('짝수')

print('-' * 30)

# 두 개의 정수 중에서 큰 수를 구해보세요.
# 10은 20보다 작습니다.
su1 = 10
su2 = 20
if su1 >= su2:
    print(f'{su1}은 {su2}보다 크거나 같습니다')
else:
    print(f'{su1}은 {su2}보다 작습니다')