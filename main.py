from lib import searchSchool
from lib import findUser
from lib import hasPassword
from validatePassword import validatePassword


Usertoken = findUser.findUser(searchSchool.searchSchool("한세", "school", "01", "4")["orgCode"], "school")

if hasPassword.hasPassword(Usertoken) == False:
    print("자가진단 페이지에서 초기 비밀번호를 설정해주세요")
else:
    UserStoken = validatePassword(Usertoken)
