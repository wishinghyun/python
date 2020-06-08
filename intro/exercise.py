import random
# 1. 로또번호 추첨 5번 반복해서

# count = 0
# while count<5:
#     lotto = random.sample(range(1,46),6)
#     print(lotto)
#     count += 1

for i in range(5):
    print(sorted(random.sample(range(1,46),6)))
print("*"*30)

lotto = [sorted(random.sample(range(1,46),6)) for i in range(5)]# 반복문을 한 줄로 출력
print(lotto)

# 2. 음식점 이름(key), 전화번호(val)인 딕셔너리

food = {
    '한식' : '02-0000-0101',
    '중식' : '02-1111-0202',
    '양식' : '02-2222-0303'
}

# 2-1 그 중에서 무작위 음식점 하나 뽑아서
pick = random.choice(list(food.keys()))
print(pick)

# 2-2 가게이름이랑 전화번호 출력
print('가계이름은',pick)
print('전화번호는',food[pick])

# f-string (파이썬 스러움)
print(f'가게이름은 {pick},전화번호는 {food[pick]}')