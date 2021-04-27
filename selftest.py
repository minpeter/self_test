from searchSchool import searchSchool
from findUser import findUser
from hasPassword import hasPassword
from validatePassword import validatePassword
from selectUserGroup import selectUserGroup
from getUserInfo import getUserInfo
from registerServey import registerServey

def selftest(schoolname, studentname, studentbirth, pw, logintype, schoolcode, schoollevel, schoolurl):
    
    print(f"===============USER:{studentname}===============")
    
    searchSchoolR = searchSchool(schoolname, logintype, schoolcode, schoollevel)
    if searchSchoolR == 0:
        return "can't school find"

    orgCode = searchSchoolR
    print(f"학교분류코드:{orgCode}")
        
    findUserR = findUser(orgCode, logintype, studentname, studentbirth, schoolurl)
    if findUserR == 0:
        return "can't user find"
    
    Utoken = findUserR
    print(f"사용자고유토큰:{Utoken}")

    if hasPassword(Utoken, schoolurl) == False:
        return "user don't have passorwd"
    
    validatePasswordR = validatePassword(Utoken, pw, schoolurl)
    if validatePasswordR == 0:
        return "Passwords do not match"

    VPtoken = validatePasswordR
    print(f"비밀번호검증성공:{VPtoken}")
    
    selectUserGroupR = selectUserGroup(VPtoken, schoolurl)
    if selectUserGroupR == 0:
        return "Technical defect"

    sugResponseV = selectUserGroupR
    print(f"유저고유번호:{sugResponseV[1]}")

    getUserInfoR = getUserInfo(sugResponseV[0],orgCode,sugResponseV[1], schoolurl)
    if getUserInfoR == 0:
        return "Technical defect"

    token = getUserInfoR
    print(f"자가진단요청 유저 고유토큰:{token}")
    
    registerServeyR = registerServey(schoolname, token, schoolurl)
    if registerServeyR == 0:
        return "Technical defect"
        
    return f"{studentname} 학생 자가진단에 성공하였습니다."