sample_list = list(range(31))
print(sample_list)
print(sample_list[3])
print(sample_list[3:24]) # 3번부터 24번 전까지 (3~23)
print(sample_list[5:-1]) # 5번부터 마지막 전까지
print(sample_list[5:]) # 끝까지 출력
print(sample_list[3:len(sample_list):2])

# 생략하기
print(sample_list[:13:2])
print(sample_list[::-1]) # 뒤에서 반대로 출력