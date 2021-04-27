import requests
import json

def registerServey(name, token, URL):
    URL = f'https://{URL}hcs.eduro.go.kr/registerServey'
      
    datas = {
        "deviceUuid":"",
        "rspns00":"Y",
        "rspns01":"1",
        "rspns02":"1",
        "rspns03":None,
        "rspns04":None,
        "rspns05":None,
        "rspns06":None,
        "rspns07":None,
        "rspns08":None,
        "rspns09":"0",
        "rspns10":None,
        "rspns11":None,
        "rspns12":None,
        "rspns13":None,
        "rspns14":None,
        "rspns15":None,
        "upperToken":str(token),
        "upperUserNameEncpt":str(name)
    }

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
        }

    #response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)

    response = requests.post(URL, headers=headers, data=json.dumps(datas)).text
    if "registerDtm" in response and "inveYmd" in response:
        print("자가진단 post 성공")
        return response
    else:
        print("자가진단 post 실패")
        return 0