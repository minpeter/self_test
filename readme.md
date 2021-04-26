+ personalData.json 파일 수정후 main.py실행시 바로 자가진단수행
+ personalData.json은 눈치것 본인의 정보로 수정하도록하자
+ encrypt.py error발생시 'pip install rsa' 을 입력하여 ras 라이블러리를 설치하자

main.py을 실행하면 바로 자가진단을 수행하므로 personalData을 HTTP로 전송받은뒤 자동으로 자가진단해주는 api 개발이나 해당 프로그램을 특정시간에 작동시키도록 스크립트나 crontab에 등록후 활용할 개획

++api개발시 디스코드봇으로도 개발할 예정

userdata 폴더안에 user0data.json, user1data.json식으로 유저데이터를 입력한후
main.py의 userUNM을 사용유저수만큼 수정후 main.py실행