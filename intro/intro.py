#print("Hello,World");
# 저장, 조건, 반복
# 1. 저장
# int? str? bool?
number = 10
string = "string"
string2 = "10"
boolean = True
print(number,string2,boolean)
# 2. 리스트 저장
# [] 안에 있으면 리스트라고 한다.
arr = [number, string, boolean]
arr_2 = [10, "10", True ,number]  
print(arr_2)
# 2-1. 인덱스로 접근하기
print(arr_2[0], arr_2[1], arr_2[2])
print(type(arr_2[0]), type(arr_2[1]), type(arr_2[2]))
# 3. dictionary {key - value}
mask = {
    '삼성' : 100,
    '역삼' : 50,
    '선릉' : 30,
    '영등포' : 10,
}
print(mask)
# 변수에 다른 값을 저장했다. 다른 값일까?
#print
