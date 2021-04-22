import requests
import json

def hasPassword(token):
    URL = 'https://senhcs.eduro.go.kr/v2/hasPassword'

    headers = {
        "Authorization": token,
        'Content-Type': 'application/json; charset=utf-8'
    }

    datas = {
        
    }
    response = requests.post(URL, headers=headers, data=json.dumps(datas)).text
    
    return response

#예제 print(hasPassword(token(findUser의 리턴값)))

