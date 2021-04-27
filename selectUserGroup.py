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
    response = response[0] #api리턴값이 이상해서 수정...

    if "token" in response and "userPNo" in response:
        print("유저그룹선택성공")
        return response["token"], response["userPNo"]
    else:
        print("유저그룹선택실패")
        return 0

#예제 print(selectUserGroup(token(findUser의 리턴값)))

