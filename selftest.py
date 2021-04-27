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
        print(f"해당교육청에{schoolname}이란 이름의 학교가 존재하지않습니다")
        print("해당유저의 학교정보를 수정해주세요")
    else:
        orgCode = searchSchoolR
        print(f"학교분류코드:{orgCode}")
            
        findUserR = findUser(orgCode, logintype, studentname, studentbirth, schoolurl)
        if findUserR == 0:
            print("입력하신정보와 일치하는 유저를 발견하는데 실패했습니다.")
            print("다음유저를 불러오거나 프로그램이 중지됩니다")
            print("error code can't user find.... 678")
        else:
            Utoken = findUserR
            print(f"사용자고유토큰:{Utoken}")

            if hasPassword(Utoken, schoolurl) == False:
                print("자가진단 페이지에서 초기 비밀번호를 설정해주세요")
                print("다음유저를 불러오거나 프로그램이 중지됩니다")
                print("error code user don't have passwd.... 188")
            else:
                validatePasswordR = validatePassword(Utoken, pw, schoolurl)
                if validatePasswordR == 0:
                    print("로그인을 시도하는 유저와 비밀번호가 일치하지않습니다")
                    print("error code Passwords do not match.... 943")
                else:
                    VPtoken = validatePasswordR
                    print(f"비밀번호검증성공:{VPtoken}")
                    
                    selectUserGroupR = selectUserGroup(VPtoken, schoolurl)
                    if selectUserGroupR == 0:
                        print("기술적인 문제가 발생했습니다.... 잠시만 기다려주세요")
                        print("error code Technical defect.... 380")
                    else:
                        sugResponseV = selectUserGroupR
                        print(f"유저고유번호:{sugResponseV[1]}")

                        getUserInfoR = getUserInfo(sugResponseV[0],orgCode,sugResponseV[1], schoolurl)
                        if getUserInfoR == 0:
                            print("기술적인 문제가 발생했습니다.... 잠시만 기다려주세요")
                            print("error code Technical defect.... 380")
                        else:
                            token = getUserInfoR
                            print(f"자가진단요청 유저 고유토큰:{token}")
                            
                            registerServeyR = registerServey(schoolname, token, schoolurl)
                            if registerServeyR == 0:
                                print("기술적인 문제가 발생했습니다.... 잠시만 기다려주세요")
                                print("error code Technical defect.... 380")
                            else:
                                print(f"{studentname} 학생 자가진단에 성공하였습니다.")