from lt import lottos

pick = lottos.lotto(100000)
print(pick)

#1. 만약 4등 한적이 있으면 4th >= 1,
count = pick['4th']
if count >= 1:
#2. 4등 몇 번 했습니다
    print(f"4등 {count} 번 했습니다")
else:
    print("fail")