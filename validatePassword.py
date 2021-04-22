import requests
import json

def validatePassword(Usertoken):
    URL = 'https://senhcs.eduro.go.kr/v2/validatePassword'

    headers = {
        "Authorization": Usertoken,
        'Content-Type': 'application/json'
    }

    datas = {
        "deviceUuid": "",
        "password": "nKqz2Cm34WOn2szagD59sNvirMq9HobEIDiEoMmyaD8r4+DgIaxM6A0nQxgyjAvY1W9AAb5vlsrPMKodBQSDqfS5AUMHTYNcSuRx5anRHCOE5cwKiRprf0qhD2Hw6sU5tTd1USUzwoo5JMavv7pn+pyYC9llHCxbl83SgnqM3dYN8bfUdnVc33lzxkK8v9pi+SMixL0ofMilgd4Rfe2zQt5Ja/ufZ2kpmb8WDpuD4NDhJG5SbkAM4Kd4vMUT75VxWwebmgAvzROEL341SyZts0afgCQCTOjfu0RRhPtIM3FARFZKKC+LC8FSARmm/t62fVa3RRE2eROU0BaSgloghA=="
    }
    response = requests.post(URL, headers=headers, data=json.dumps(datas)).text
    
    return response

#예제 print(validatePassword(token(findUser의 리턴값)))

