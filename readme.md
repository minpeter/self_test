# 라이브러리 설치
* pip install rsa
* pip install requests

python3 필요(f-string문법)

# 설치순서
1. userdata 폴더 생성
2. userdata 폴더안에 user0data.json,  user1data.json등 파일 생성
3. user*data.json 안에 내용작성
```json
{
    "schoolName": "학교이름",
    "studentName": "학생이름",
    "studentBirth": "생년월일 ex)050611",
    "schoolRegion": "교육청이름 ex)서울,경기도",
    "schoolType": "학교급 ex)중학교,고등학교",
    "password" : "자가진단 비번"
}
```
4. python3 main.py

추가로 rontab 같은 명령으로 등록해두면 아침마다 자동으로 자가진단을 하도록 할수있다.
