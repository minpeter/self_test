import requests
import json

def getUserInfo(token,orgCode,userPNo, URL):
    URL = f'https://{URL}hcs.eduro.go.kr/v2/getUserInfo'

    datas = {
        'orgCode': 'B100000662',
        'userPNo': '2021000076'
        }

    headers = {
        "Authorization": token,
        'Content-Type': 'application/json'
    }
    response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)
    return response["token"]
# 예제 print(getUserInfo(token))
