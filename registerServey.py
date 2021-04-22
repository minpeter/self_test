import requests
import json

def registerServey(name, token):
    URL = 'https://senhcs.eduro.go.kr/registerServey'
      
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

    return requests.post(URL, headers=headers, data=json.dumps(datas)).text
    