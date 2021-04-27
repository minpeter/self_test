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
    
    if "isError" in response:
        print("비밀번호 인증 실패")
        return 0
    else:
        print(f"데이터와 일치하는 유저를 발견했습니다")
        print("비밀번호가 일치합니다")
        print(response)
        return response

#예제 print(validatePassword(token(findUser의 리턴값)))

