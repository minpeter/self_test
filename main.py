from lib import searchSchool
from lib import findUser
from registerServey import registerServey



UserInfo = findUser.findUser(searchSchool.searchSchool("한세", "school", "01", "4")["orgCode"], "school")

print(UserInfo)

#registerServey(UserInfo["userName"], UserInfo["token"])