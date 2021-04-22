import requests


def getUserInfo():
    URL = 'https://senhcs.eduro.go.kr/v2/getUserInfo'

    datas = {
        'orgCode': 'B100000662',
        'userPNo': '2021000076'
        }
    headers = {

    }
    cookies = {
        
    }
    response = requests.post(URL, data=datas, verify=False)
    print('CODE:')
    print(response.status_code)
    return response.text

# 예제 
print(getUserInfo())
