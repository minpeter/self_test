from searchSchool import searchSchool
from findUser import findUser
from hasPassword import hasPassword
from validatePassword import validatePassword
from selectUserGroup import selectUserGroup
from getUserInfo import getUserInfo
from registerServey import registerServey
from mapping import schoolinfo

import json

with open('personalData.json', 'r') as f:
    json_data = json.load(f)

schoolName = json_data["schoolName"]
studentName = json_data["studentName"]
studentBirth = json_data["studentBirth"]
loginType = json_data["loginType"]
schoolRegion = json_data["schoolRegion"]
schoolType = json_data["schoolType"]
password = json_data["password"]


info = schoolinfo(schoolRegion,schoolType)

schoolcode = info["schoolcode"]
schoollevel = info["schoollevel"]
schoolurl = info["schoolurl"]


orgCode = searchSchool(schoolName, loginType, schoolcode, schoollevel)

Utoken = findUser(orgCode, loginType, studentName, studentBirth, schoolurl)
print("사용자고유토큰:"+Utoken)

if hasPassword(Utoken, schoolurl) == False:
    print("자가진단 페이지에서 초기 비밀번호를 설정해주세요")
else:
    VPtoken = validatePassword(Utoken,password, schoolurl)
    print("로그인성공:"+VPtoken)
    sugResponse = selectUserGroup(VPtoken, schoolurl)
    print(sugResponse)
    token = getUserInfo(sugResponse[0],orgCode,sugResponse[1], schoolurl)
    print("유저식별성공:"+token)
    print("자가진단에 성공하였습니다."+registerServey(schoolName, token, schoolurl))
    

    