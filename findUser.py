import requests
import json
import encrypt

def findUser(orgCode, loginType, name, birthday):
    URL = 'https://senhcs.eduro.go.kr/v2/findUser'
    
    datas = {
        "orgCode": orgCode,
        "name":encrypt.encrypt(name),
        "birthday":encrypt.encrypt(birthday),
        "stdntPNo":None,
        "loginType": loginType
    }

    headers = {'Content-Type': 'application/json'}

    response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)
    print(response)
    return response["token"]

#예제 print(findUser("B100000662", "school"))
