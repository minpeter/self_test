import requests
import json

def findUser(orgCode, loginType):
    URL = 'https://senhcs.eduro.go.kr/v2/findUser'
    
    datas = {
        "orgCode":str(orgCode),
        "name":"yynufL42/4wvEQB/keO/9xynwXKCHXQiPbOHkR+DnH1RP0vF97rUz0flFFnc7JYpmEJ0RqMD+8YM/T0vyDPhgmVY7o0dW+mBrzMjS0IJaTp8VKjkpO/9hL64aC2FXvnXpyFXq6zwiKcKMZqcLaltBY/3EvFvS+bo1xOsvqXJjsGrPyle1Axqh15pbv9JSr4YmS8ykskkU1DJ0EK8Y0nnWdKAvJNp6vgenwVwszysjqnjyOswb6VoshekoS9P/CDUWGy25pjRuEQ2TwvKfTGG+qe9TKTt7uOCJFnzGpc6C82Zo+DvztwA+w3S8NpzXl3X8jvfGhMadYmNicp46Mnrxw==",
        "birthday":"QCy0zoMCN4B/wK5cAVOg5Cc0C4SQG0hpuVdTlal4kuJ1hOy8XaQKGierR+RAkvGqZzg7pX3BegfhWGVyyBCiGn5R+lKMZjcrDvA9Ybj0LaKJ+zJkMhcGjXPOhFDprGeCBaCquHubZfDxALo2/FANmSMX8Boe7RJoZNoR9a72Ephcy9CukfWlYK4dNWPigSQ89FcLLnBF4vLoPTAInYEsn6XSg9Eue9QqyzTSWix8rdjNwIYvqwDZEaojlkNwXhek7QVufFRCtE9UGNCtfyTJg2FsorZAfiizjtqgZK+BMrLwQfAYXHpA90ADoLUpfKtiDDyR3YbMRYZnMZDNG+kVSg==",
        "stdntPNo":None,
        "loginType":str(loginType)
    }

    headers = {'Content-Type': 'application/json; charset=utf-8'}

    response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)
    return response

# 예제 print(findUser())
