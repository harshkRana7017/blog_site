from datetime import datetime, timedelta
import jwt
SECRET_KEY='HARSH_RANA'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRES_MINUTES=15


def create_acess_token(data: dict):
    to_encode= data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(access_token: str):
    try:
        payload=  jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None

    