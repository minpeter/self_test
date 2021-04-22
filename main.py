from lib import searchSchool
from lib import findUser
from lib import hasPassword
from lib import validatePassword
from selectUserGroup import selectUserGroup
from getUserInfo import getUserInfo

token = findUser.findUser(searchSchool.searchSchool("한세", "school", "01", "4")["orgCode"], "school")

if hasPassword.hasPassword(token) == False:
    print("자가진단 페이지에서 초기 비밀번호를 설정해주세요")
else:
    token = validatePassword.validatePassword(token)
    token = selectUserGroup(token)
    getUserInfo(token)
    