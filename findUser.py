import requests
import json
from encrypt import encrypt

def findUser(orgCode, loginType, name, birthday, URL):
    URL = f'https://{URL}hcs.eduro.go.kr/v2/findUser'
    
    datas = {
        "orgCode": orgCode,
        "name": encrypt(name),
        "birthday": encrypt(birthday),
        "stdntPNo": None,
        "loginType": loginType
    }
    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)
    print(response)
    return response["token"]

#예제 print(findUser("B100000662", "school"))
