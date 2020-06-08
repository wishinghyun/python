import requests
from pprint import pprint
key = 'AIzaSyDTSpq9vrGsRVciS5ol-d8fPPWIEph5xBs'
# string interpolation 사용
search = input("검색어를 입력해 주세요 : ")
q = f'q={search}'
my_type = 'type=video'
part = 'part=snippet'
maxResults = 'maxResults=20'

url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}%{q}&{maxResults}'

response = requests.get(url)
datas = response.json()

# 채널명, 영상 제목
for data in datas['items'][:10]:
    print(data['snippet']['title'], end=' /채널명 ') # end 붙이면 2개의 print가 한 줄로 출력됨
    print(data['snippet']['channelTitle'])