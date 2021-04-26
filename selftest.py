from searchSchool import searchSchool
from findUser import findUser
from hasPassword import hasPassword
from validatePassword import validatePassword
from selectUserGroup import selectUserGroup
from getUserInfo import getUserInfo
from registerServey import registerServey

def selftest(schoolname, studentname, studentbirth, pw, logintype, schoolcode, schoollevel, schoolurl):
    orgCode = searchSchool(schoolname, logintype, schoolcode, schoollevel)

    Utoken = findUser(orgCode, logintype, studentname, studentbirth, schoolurl)
    print(f"사용자고유토큰:{Utoken}")

    if hasPassword(Utoken, schoolurl) == False:
        print("자가진단 페이지에서 초기 비밀번호를 설정해주세요")
    else:
        VPtoken = validatePassword(Utoken, pw, schoolurl)
        print(f"로그인성공:{VPtoken}")
        sugResponse = selectUserGroup(VPtoken, schoolurl)
        print(sugResponse)
        token = getUserInfo(sugResponse[0],orgCode,sugResponse[1], schoolurl)
        print(f"유저식별성공:{token}")
        registerServey(schoolname, token, schoolurl)
        print("자가진단에 성공하였습니다.")