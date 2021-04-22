import requests
import json

def selectUserGroup(UserStoken):
    URL = 'https://senhcs.eduro.go.kr/v2/selectUserGroup'

    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlhdCI6MTYxOTA3MDMxNDIxOH0.eyJubyI6IjIwMjEwMDAwNzYiLCJzZWNyZXRLZXkiOiJqbTV6Iiwib3JnIjoiQjEwMDAwMDY2MiIsImV4cCI6MTY1MDYwNjMxNCwicm4iOiJudWxsIiwiaWF0IjoxNjE5MDcwMzE0MjE4fQ.E9AeQgJIM4EWdhiJsei6RANnFi_mEG-av0KRB8psBG0",
        'Content-Type': 'application/json'
    }

    datas = {
        
    }
    response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)
    
    return response[0]["token"]

#예제 print(selectUserGroup(token(findUser의 리턴값)))

