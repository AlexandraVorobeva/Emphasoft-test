from fastapi import APIRouter, Depends, Response, status

from models.users import User, UserCreate, UserUpdate
from services.users import UserService
from services.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[User])
def get_all_users(
    service: UserService = Depends(),
    user: User = Depends(get_current_user),
):
    """
    GET information about all users.
    \f
    :param service: business logic
    :param user: authenticated user
    """
    return service.get_list()


@router.post("/", response_model=User)
def create_user(
    user_data: UserCreate,
    user: User = Depends(get_current_user),
    service: UserService = Depends(),
):
    """
    POST information about new user.
    \f
    :param user_data: new user info
    :param service: business logic
    :param user: authenticated user
    """
    return service.create(user_data)


@router.get("/{user_id}", response_model=User)
def get_user(
    user_id: int,
    user: User = Depends(get_current_user),
    service: UserService = Depends(),
):
    """
    GET information about any user by id.
    \f
    :param user_id: id of user
    :param service: business logic
    :param user: authenticated user
    """
    return service.get(user_id)


@router.put("/{user_id}", response_model=User)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    user: User = Depends(get_current_user),
    service: UserService = Depends(),
):
    """
    UPDATE information about any user by id.
    \f
    :param user_id: id of user
    :param user_data: new info about user
    :param service: business logic
    :param user: authenticated user
    :return:
    """
    return service.update(user_id, user_data)


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    user: User = Depends(get_current_user),
    service: UserService = Depends(),
):
    """
    DELETE information about any user by id.
    \f
    :param user_id: id of user
    :param service: business logic
    :param user: authenticated user
    """
    service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
