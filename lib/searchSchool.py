import requests
import json

def searchSchool(schoolname, loginType, lctnScCode, schulCrseScCode):
    URL = 'https://hcs.eduro.go.kr/v2/searchSchool'
    
    paramDict = {
        'lctnScCode' : '01',    #교육청코드 01(서울), 02(부산), 03(대구), 04(인천), 05(광주), 06(대전), 07(울산), 08(세종), 10(경기도), 11(강원), 12(충청북), 13(충청남), 14(전라북), 15(전라남), 16(경상북), 17(경상남), 18(제주) (로그인타입이 학교일떄만)
        'schulCrseScCode' : '4',    #학교종류코드 1(유치원), 2(초등학교), 3(중학교), 4(고등학교), 5(특수학교) (로그인타입이 학교일떄만)
        'orgName' : str(schoolname),    #검색할 학교 이름
        'loginType' : str(loginType)    #로그인타입 school(학교), univ(대학교), office(교육행정기관 등)
    }

    response = json.loads(requests.get(URL, params=paramDict).text)
    
    if response["schulList"] == []:
        return "error"
    else:
        return response["schulList"][0]["orgCode"]


# 예제 print(searchSchool("한세", "school", "01", "4"))
