from mapping import schoolinfo
from selftest import selftest
import json

userNUM = 3

def calljson(jsonfilename):
    with open(f'userdata/{jsonfilename}.json', 'r') as f:
        json_data = json.load(f)

    schoolName = json_data["schoolName"]
    studentName = json_data["studentName"]
    studentBirth = json_data["studentBirth"]
    schoolRegion = json_data["schoolRegion"]
    schoolType = json_data["schoolType"]
    password = json_data["password"]

    schoolinfoR =  schoolinfo(schoolRegion,schoolType)
    if schoolinfoR == 0:
        print("교육청 학교 정보 맵핑 실패")
    else:
        print("교육청 학교 정보 맵핑 성공")
        info = schoolinfoR

        schoolCode = info["schoolcode"]
        schoolLevel = info["schoollevel"]
        schoolUrl = info["schoolurl"]

        loginType = "school"

        msg = selftest(schoolName, studentName, studentBirth, password, loginType, schoolCode, schoolLevel, schoolUrl)
        print(msg)

for i in range(userNUM):
            calljson(f"user{i}data")
