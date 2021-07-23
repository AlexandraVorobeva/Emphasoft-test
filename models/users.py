from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseUser):
    pass


class UserUpdate(BaseUser):
    pass
