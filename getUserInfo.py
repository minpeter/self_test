import requests
import json

def getUserInfo(token,orgCode,userPNo, URL):
    URL = f'https://{URL}hcs.eduro.go.kr/v2/getUserInfo'

    datas = {
        'orgCode': orgCode,
        'userPNo': userPNo
        }

    headers = {
        "Authorization": token,
        'Content-Type': 'application/json'
    }
    response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)
    
    if "token" in response:
        print("로그인성공")
        return response["token"]
    else:
        print("로그인실패")
        return 0
# 예제 print(getUserInfo(token))
