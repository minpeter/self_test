import requests
import json
import encrypt


def validatePassword(token):
    URL = 'https://senhcs.eduro.go.kr/v2/validatePassword'

    headers = {
        "Authorization": token,
        'Content-Type': 'application/json'
    }

    datas = {
        "deviceUuid": "",
        "password": encrypt.encrypt("050611")
    }

    response = requests.post(URL, headers=headers, data=json.dumps(datas)).text
    
    return response

#예제 print(validatePassword(token(findUser의 리턴값)))

