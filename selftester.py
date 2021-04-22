import json
import requests 
URL = '1' 
response = requests.get(URL) 
response.status_code 
response.text

datas = {
  deviceUuid: '',
  rspns00: 'Y',
  rspns01: '1',
  rspns02: '1',
  rspns03: None,
  rspns04: None,
  rspns05: None,
  rspns06: None,
  rspns07: '0',
  rspns08: '0',
  rspns09: '0',
  rspns10: None,
  rspns11: None,
  rspns12: None,
  rspns13: None,
  rspns14: None,
  rspns15: None
}
    upperToken: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlhdCI6MTYxNjQ3MTAzOTU2Nn0.eyJubyI6IjIwMjEwMDAwNzYiLCJzZWNyZXRLZXkiOiJWYzllIiwib3JnIjoiQjEwMDAwMDY2MiIsImV4cCI6MTY0ODAwNzAzOSwicm4iOiIwIiwiaWF0IjoxNjE2NDcxMDM5NTY2fQ.KT-CS9oXsruIXyPRqCKxz9gwX8iXgfpiFLJiHXsSq8Q"
    upperUserNameEncpt: "민웅기"
}
res = requests.post(URL, data=data)

res.request # 내가 보낸 request 객체에 접근 가능 
res.status_code # 응답 코드 
res.raise_for_status() # 200 OK 코드가 아닌 경우 에러 발동 
res.json() # json response일 경우 딕셔너리 타입으로 바로 변환


publicKey = '30820122300d06092a864886f70d01010105000382010f003082010a0282010100f357429c22add0d547ee3e4e876f921a0114d1aaa2e6eeac6177a6a2e2565ce9593b78ea0ec1d8335a9f12356f08e99ea0c3455d849774d85f954ee68d63fc8d6526918210f28dc51aa333b0c4cdc6bf9b029d1c50b5aef5e626c9c8c9c16231c41eef530be91143627205bbbf99c2c261791d2df71e69fbc83cdc7e37c1b3df4ae71244a691c6d2a73eab7617c713e9c193484459f45adc6dd0cba1d54f1abef5b2c34dee43fc0c067ce1c140bc4f81b935c94b116cce404c5b438a0395906ff0133f5b1c6e3b2bb423c6c350376eb4939f44461164195acc51ef44a34d4100f6a837e3473e3ce2e16cedbe67ca48da301f64fc4240b878c9cc6b3d30c316b50203010001';
