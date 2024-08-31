from pydantic import BaseModel

class User(BaseModel):
    userame:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type: str