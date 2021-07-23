from pydantic import BaseModel
from models.users import BaseUser


class UserRegistrar(BaseUser):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'