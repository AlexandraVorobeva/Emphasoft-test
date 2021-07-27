from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_session
import tables
from models.users import UserCreate, UserUpdate


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int) -> tables.User:
        """
        GET information from database.

        :param user_id: user id
        :return: database instance
        """
        user = self.session.query(tables.User).filter_by(id=user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

    def get_list(self) -> list[tables.User]:
        """
        Get information about all users from database.

        :return: database instance
        """
        users = self.session.query(tables.User).all()
        return users

    def get(self, user_id: int) -> tables.User:
        """
        Get info from database about user by id.

        :param user_id:
        :return: database instance
        """
        return self._get(user_id)

    def create(self, user_data: UserCreate) -> tables.User:
        """
        Create new user in database.

        :param user_data: new info about user
        :return: database instance
        """
        user = tables.User(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_id: int, user_data: UserUpdate) -> tables.User:
        """
        Update info about any user in database>

        :param user_id:  user id
        :param user_data: new info about user
        :return: database instance
        """
        user = self._get(user_id)
        for field, value in user_data:
            setattr(user, field, value)
        self.session.commit()
        return user

    def delete(self, user_id: int):
        """
        Delete information about any user by id.

        :param user_id: user id
        """
        user = self._get(user_id)
        self.session.delete(user)
        self.session.commit()
