from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.users import User
from models.auth import UserRegistrar, Token
from services.users import UserService
from services.auth import AuthService, get_current_user


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/sign-up/', response_model=Token)
def sing_up(user_data: UserRegistrar, service: AuthService = Depends()):
    return service.register_new_user(user_data)


@router.post('/sign-in/', response_model=Token)
def sing_in(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service: AuthService = Depends()
):
    return service.authenticate_user(
        form_data.username,
        form_data.password
    )


@router.get('/user/', response_model=User,)
def get_user(user: User = Depends(get_current_user)):
    return user