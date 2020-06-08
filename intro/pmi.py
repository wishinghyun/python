import requests
#import pprint
from pprint import pprint

def pmi(params):
    url = f'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address={params}'
    response = requests.get(url).json()
    #response['stores'][:3] #[:10] 는 리스트일때 앞에서부터 10개만 가져옴 [2:10] 2번부터 10개
    remain = ['plenty','some','few','empty','break']
    mask_info = {} #mask_info라는 dict 생성
    for data in response['stores'][:10]:
        if data['remain_stat'] == remain[0]:
            mask_info[data['name']] = '100개 이상'
        elif data['remain_stat'] == remain[1]:
            mask_info[data['name']] = '30개 이상'
        elif data['remain_stat'] == remain[2]:
            mask_info[data['name']] = '2개 이상'
        elif data['remain_stat'] == remain[3]:
            mask_info[data['name']] = '1개 이하'
        else:
            mask_info[data['name']] = '판매중지'
    return mask_info

params = input('주소를 시 구 동으로 입력해주세요 : ')
mask = pmi(params)
#pprint.pprint(mask)

for key, val in mask.items():
    print(f'{key}판매처에 마스크가 {val} 있습니다')