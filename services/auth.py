from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from models.users import User
from tables import User as table_user
from models.auth import Token, UserRegistrar
from settings import jwt_secret, jwt_algorithm
from database import get_session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign-in/")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    Get information about current user.

    :param token: token
    :return: model of user
    """
    return AuthService.validate_token(token)


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        """
        Check if a password is correct.

        :param plain_password: currently password
        :param hashed_password: hash of password
        :return: True in case of success, False otherwise
        """
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(self, password: str) -> str:
        """
        Create hash of password.

        :param password: password
        :return: hash of password
        """
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        """
        Check if a token is valid.

        :param token: token
        :return: model of user
        """
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                token,
                jwt_secret,
                algorithms=[jwt_algorithm],
            )
        except JWTError:
            raise exception from None

        user_data = payload.get("user")

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exception from None
        return user

    @classmethod
    def create_token(cls, user: table_user) -> Token:
        """
        Create token for information about any user.

        :param user: user info
        :return: token
        """
        user_data = User.from_orm(user)
        payload = {
            "user": user_data.dict(),
        }
        token = jwt.encode(
            payload,
            jwt_secret,
            algorithm=jwt_algorithm,
        )
        return Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_new_user(self, user_data: UserRegistrar) -> Token:
        """
        Register new user by adding information about him in database.

        :param user_data:
        :return: token
        """
        user = table_user(
            email=user_data.email,
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            password_hash=self.hash_password(user_data.password),
        )

        self.session.add(user)
        self.session.commit()

        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> Token:
        """
        Authenticating an existing user.

        :param username: name of user
        :param password: password of user
        :return: token
        """
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

        user = (
            self.session.query(table_user)
            .filter(table_user.username == username)
            .first()
        )
        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)
