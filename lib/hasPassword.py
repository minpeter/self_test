import requests
import json

def hasPassword(Usertoken):
    URL = 'https://senhcs.eduro.go.kr/v2/hasPassword'

    headers = {
        "Authorization": Usertoken,
        'Content-Type': 'application/json; charset=utf-8'
    }

    datas = {
        
    }
    response = requests.post(URL, headers=headers, data=json.dumps(datas)).text
    
    return response

#예제 print(hasPassword(token(findUser의 리턴값)))

