from mapping import schoolinfo
from selftest import selftest
import json

userNUM = 5

def calljson(jsonfilename):
    with open(f'userdata/{jsonfilename}.json', 'r') as f:
        json_data = json.load(f)

    schoolName = json_data["schoolName"]
    studentName = json_data["studentName"]
    studentBirth = json_data["studentBirth"]
    schoolRegion = json_data["schoolRegion"]
    schoolType = json_data["schoolType"]
    password = json_data["password"]


    info = schoolinfo(schoolRegion,schoolType)

    schoolCode = info["schoolcode"]
    schoolLevel = info["schoollevel"]
    schoolUrl = info["schoolurl"]

    loginType = "school"

    selftest(schoolName, studentName, studentBirth, password, loginType, schoolCode, schoolLevel, schoolUrl)


for i in range(userNUM):
    calljson(f"user{i}data")
