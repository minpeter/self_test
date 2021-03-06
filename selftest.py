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
    print(f"π νκ΅λΆλ₯μ½λ:{orgCode}")
        
    findUserR = findUser(orgCode, logintype, studentname, studentbirth, schoolurl)
    if findUserR == 0:
        return "can't user find"
    
    Utoken = findUserR
    print(f"π μ¬μ©μκ³ μ ν ν°:{Utoken}")

    if hasPassword(Utoken, schoolurl) == False:
        return "user don't have passorwd"
    
    validatePasswordR = validatePassword(Utoken, pw, schoolurl)
    if validatePasswordR == 0:
        return "Passwords do not match"

    VPtoken = validatePasswordR
    print(f"λΉλ°λ²νΈκ²μ¦μ±κ³΅:{VPtoken}")
    
    selectUserGroupR = selectUserGroup(VPtoken, schoolurl)
    if selectUserGroupR == 0:
        return "Technical defect"

    sugResponseV = selectUserGroupR
    print(f"μ μ κ³ μ λ²νΈ:{sugResponseV[1]}")

    getUserInfoR = getUserInfo(sugResponseV[0],orgCode,sugResponseV[1], schoolurl)
    if getUserInfoR == 0:
        return "Technical defect"

    token = getUserInfoR
    print(f"μκ°μ§λ¨μμ²­ μ μ  κ³ μ ν ν°:{token}")
    
    registerServeyR = registerServey(schoolname, token, schoolurl)
    if registerServeyR == 0:
        return "Technical defect"
        
    return f"{studentname} νμ μκ°μ§λ¨μ μ±κ³΅νμμ΅λλ€."