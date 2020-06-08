# 1. 출력해보기
print('Hello, World!')

# 프로그래밍 언어의 기본 3가지
#1. 변수 저장 - 무엇을 저장 할 수 있을까?
number = 10
string = '10'
boolean = True
# 파이썬에는 값이 없음을 표현하는 None 타입이 존재
nothing = None
print(number, string, boolean, nothing)
print(type(nothing))

#1-1 정수형
number = 10
float_num = 1.3
complex_num = (3 + 3j)
print(type(number), type(float_num), type(complex_num))

# 2 bool
print(type(True))
print(type(False))
# 0, 0.0, [], {}
print(False == 0)

# 3 문자형
# '', ""
greeing = 'hi'
name = "kim"
print(greeing, name)

# 문자열 입력 받기
# input()
age = input("나이를 입력해 주세요 : ")
print(type(age))
print(type(int(age)))

# string interpolation
name = 'kim'
print('안녕하세요, ', name)
print('{}, {}'.format(greeing, name)) #3.5 버전 이하에서도 가능
print(f'{greeing}, {name}') #3.6버전 이후부터 가능

# 연산과 출력 형태 지정
pi = 3.141592
print(f'원주율은 {pi:.4}. 반지름 = 2 원의 넓이는 {pi*2*2}') # {pi:.4}는 pi의 소수점 4번째 자리까지 표기