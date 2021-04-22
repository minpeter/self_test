from lib import searchSchool
import findUser
from lib import hasPassword
from lib import validatePassword
from selectUserGroup import selectUserGroup
from getUserInfo import getUserInfo
import encrypt
from registerServey import registerServey


token = findUser.findUser(searchSchool.searchSchool("한세", "school", "01", "4")["orgCode"], "school", "민웅기", "050611")
print(token)
if hasPassword.hasPassword(token) == False:
    print("자가진단 페이지에서 초기 비밀번호를 설정해주세요")
else:
    token = validatePassword.validatePassword(token)
    print(token)
    token = selectUserGroup(token)
    print(token)
    token = getUserInfo(token)
    print(token)
    print(registerServey("민웅기",token))

    