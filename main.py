from searchSchool import searchSchool
from findUser import findUser
from registerServey import registerServey



UserInfo = findUser(searchSchool("한세사이버보안고등학교", "school")["orgCode"], "school")

registerServey(UserInfo["userName"], UserInfo["token"])