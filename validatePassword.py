import requests
import json
from encrypt import encrypt


def validatePassword(token, pw, URL):
    URL = f'https://{URL}hcs.eduro.go.kr/v2/validatePassword'

    headers = {
        "Authorization": token,
        'Content-Type': 'application/json'
    }

    datas = {
        "deviceUuid": "",
        "password": encrypt(pw)

        #encrypt(pw)
    }

    response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)
    
    return response

#예제 print(validatePassword(token(findUser의 리턴값)))

