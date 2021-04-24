import requests
import json

def selectUserGroup(token, URL):
    URL = f'https://{URL}hcs.eduro.go.kr/v2/selectUserGroup'

    headers = {
        "Authorization": token,
        'Content-Type': 'application/json;charset=UTF-8'
    }

    datas = {
        
    }

    response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)
    
    return response[0]["token"], response[0]["userPNo"]

#예제 print(selectUserGroup(token(findUser의 리턴값)))

