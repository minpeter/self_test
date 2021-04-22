import requests
import json

def registerServey(name, token):
    URL = 'https://senhcs.eduro.go.kr/registerServey'
      
    datas = {
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
        "rspns00":"Y",
        "deviceUuid":"",
        "upperToken":str(token),
        "upperUserNameEncpt":str(name)
    }

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
        }

    #response = json.loads(requests.post(URL, headers=headers, data=json.dumps(datas)).text)

    print(requests.post(URL, headers=headers, data=datas).text)
    return 0