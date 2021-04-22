import requests
import json
import encrypt

def findUser(orgCode, loginType, name, birthday):
    URL = 'https://senhcs.eduro.go.kr/v2/findUser'
    
    datas = {
        "orgCode":str(orgCode),
        "name":encrypt.encrypt(name),
        "birthday":encrypt.encrypt(birthday),
        "stdntPNo":None,
        "loginType":str(loginType)
    }

    headers = {'Content-Type': 'application/json; charset=utf-8'}

    response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)
    return response["token"]

#예제 print(findUser("B100000662", "school"))
