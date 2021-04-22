import base64
import rsa

def encrypt(msg):
    msg = msg.encode('utf-8')

    public_key_bytes = open('pubkey/pubkey.pem', 'rb').read() # 공개키 파일을 읽기
    public_key = rsa.PublicKey.load_pkcs1_openssl_pem(keyfile=public_key_bytes) # 공개키 파일을 이용해서 공개키로 변환
    encrypted_bytes = rsa.encrypt(msg, public_key) # 공개키를 이용해서 암호화
    encrypted_msg = base64.b64encode(encrypted_bytes).decode('utf-8') # 암호화된 bytes 데이터를 string 형태로 decode
    return encrypted_msg
