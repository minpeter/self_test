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
    
    if "token" in response:
        print(f"데이터와 일치하는 유저를 발견했습니다")
        return response["token"]
    else:
        print("유저찾기실패")
        return 0
    
    

#예제 print(findUser("B100000662", "school"))
