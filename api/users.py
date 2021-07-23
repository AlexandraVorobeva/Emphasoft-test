from fastapi import APIRouter, Depends, Response, status

from models.users import User, UserCreate, UserUpdate
from services.users import UserService


router = APIRouter(prefix='/users')


@router.get('/', response_model=list[User])
def get_all_users(service: UserService = Depends()):
    return service.get_list()


@router.post('/', response_model=User)
def create_operations(
        user_data: UserCreate,
        service: UserService = Depends(),
):
    return service.create(user_data)


@router.get('/{user_id}', response_model=User)
def get_user(
        user_id: int,
        service: UserService = Depends(),
):
    return service.get(user_id)


@router.put('/{user_id}', response_model=User)
def update_user(
        user_id: int,
        user_data: UserUpdate,
        service: UserService = Depends(),
):
    return service.update(user_id, user_data)


@router.delete('/{user_id}')
def delete_user(
        user_id: int,
        service: UserService = Depends(),
):
    service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)





