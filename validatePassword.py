import requests
import json

def validatePassword():
    URL = 'https://senhcs.eduro.go.kr/v2/validatePassword'
    
    datas = {"password":"e6mCflZvNcSyd7rF2kM6v8cB+5gtoL1dTbtgzvDl17IUK08jDHHRnP5TauVs36rz/qmnJhOekDL5mfTPL8eaAqG8Kk3ik5jYZ6184l2ktiHCDC8vY+c4kmxG+XM5+eAqSVVIPjIUhsXSf2V4STH6AtfcVTJEg7bOPSb7C8I4SNU4aa9gw+cKhzeoDJZH3QUPnaeDE3OC1+uqNyeOnADrurDiaebr6/+Jh6jvYCdmgRMQxKhE6hR/Z7FEz9avOKFJPGp2v53ssSFeybmQw9Iauf/I30UW9LQpAuLH5kcfTK6icYR6AmPt7vD09eCxnmlQ5qLSxcQwWS4nXGV3DJ3pcQ==",
    "deviceUuid":""
    }

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlhdCI6MTYxODQ2NzM1OTI2OH0.eyJubyI6IjIwMjEwMDAwNzYiLCJvcmciOiJCMTAwMDAwNjYyIiwiZXhwIjoxNjUwMDAzMzU5LCJybiI6Im51bGwiLCJpYXQiOjE2MTg0NjczNTkyNjh9.vmyc8Zbe9SjoRhm2OIm8M_WlFLuARbnQlfKR-AyF0KI
    }

    response = requests.post(URL, headers=headers, data=json.dumps(datas)).text
    return response


print(validatePassword())

