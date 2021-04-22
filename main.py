from lib import searchSchool
import findUser
from lib import hasPassword
from validatePassword import validatePassword
from selectUserGroup import selectUserGroup
from getUserInfo import getUserInfo
from registerServey import registerServey
import json


with open('personalData.json', 'r') as f:
    json_data = json.load(f)

schoolName = json_data["schoolName"]
studentName = json_data["studentName"]
studentBirth = json_data["studentBirth"]
loginType = json_data["loginType"]
schoolRegion = json_data["schoolRegion"]
schoolType = json_data["schoolType"]

print(json.dumps(json_data))

orgCode = searchSchool.searchSchool(schoolName, loginType, schoolRegion, schoolType)
token = findUser.findUser(orgCode, loginType, studentName, studentBirth)
print(token)

if hasPassword.hasPassword(token) == False:
    print("자가진단 페이지에서 초기 비밀번호를 설정해주세요")
else:
    token = validatePassword(token)
    print(token)
    token = selectUserGroup(token)
    print(token)
    token = getUserInfo(token)
    print(token)
    print(registerServey("민웅기",token))

    