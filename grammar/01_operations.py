# 논리 연산자
# and, or, not
print("____and____") # 전부 true일때만 true 반환
print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("____or____") # 둘 중 하나만 true면 true 반환
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print("____not____")
print(not True)
print(not False) #0, 0.0, {}, []도 False로 표기

#in, not in
print("____in____") # 뒤에 있는 것에 앞의 것이 포함되어있는지 여부 반환
print('a' in 'apple')
print(1 not in [1,2,3])

#단축 평가
print('' or 'Text' or 'Text_2') # or연산은 처음 true가 보장이 될 경우 더이상 계산을 하지 않는다.
print('Text' and '' or 'Text_2')