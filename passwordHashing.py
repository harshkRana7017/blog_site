from passlib.context import CryptContext

pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto" )

def verify_passowrd(plain_password:str,hashedPassword:str ):
    return pwd_context.verify(plain_password, hashedPassword)

def get_hashed_passwrd(password:str):
    return pwd_context.hash(password)