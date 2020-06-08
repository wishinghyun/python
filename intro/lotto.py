import random
#print(dir(random))#dir은 함수 안에 있는 메소드 목록 보여줌

# choice를 써보자
# number = random.choice(range(10))
# print(number)

#list에서 무작위로 뽑아보자
arr = ['100', '50', '30', '20']
pick = random.choice(arr)
print(pick)

# dict에도 써보자
mask = {
    '100' : '삼성',
    '50' : '역삼',
    '30' : '선릉',
    '20' : '영등포',
}
print(mask[pick])

# sample
lotto = random.sample(range(1,46),6)#1에서 45까지의 숫자 6개 리스트 형태로
print(sorted(lotto))#sorted는 작은숫자부터 큰 숫자대로 정렬