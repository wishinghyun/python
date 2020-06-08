# 1. dictionary
# key, value로 이루어져있음
dict_a = {}
dict_b = dict()
# key가 중복이 불가능하다
dict_a = {'삼성':100,'역삼':50,'삼성':30} # key가 중복될 경우 마지막 key값만 출력
print(dict_a)

print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

# key값으로 value값 출력
print(dict_a['삼성'])
print(dict_a.get('삼성')) 

# .get과 [] 접근 차이점
dict_a = {'삼성':100,'역삼':50}
print(dict_a.get('선릉')) # key값이 없을 경우 None 리턴 (오류 안남)
#print(dict_a['선릉'])    # key값이 없을 경우 오류 발생

# 2. set
# set는 순서가 없이 저장된다
# 중복이 없다 set_a = {1, 1, 1} 하면 중복 제거된 {1}로 출력됨
set_a = {1, 3, 2}
set_b = {3, 6, 9}
print(set_a - set_b) # 앞에서 뒤에꺼 제거 후 앞에꺼 출력
print(set_a | set_b) # 합집합 중복 제거
print(set_a & set_b) # 교집합 공통 요소 출력

list_a = [1, 1, 1, 1]
print(list(set(list_a))[0]) # 리스트 중복 제거할때 set으로 바꾼뒤 list로 다시 바꾸면 됨

string = "immutable"
list_a = ['immutable?', 'real?']

print(string[0])
print(list_a[0])
#string[0] = 'a'
list_a[0] = 'mutable'
print(list_a)

# list_a = ['mutable'] # 이건 리스트에 값을 재할당한거 => list_a[0] = 'mutable'랑은 의미가 다르다

list_a = ['immutable?', 'real?']
list_b = list_a
print(list_a, list_b)
list_b[0] = 'mutable'
print(list_a, list_b)