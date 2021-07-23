from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_session
import tables
from models.users import UserCreate, UserUpdate


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int) -> tables.User:
        user = (
            self.session
                .query(tables.User)
                .filter_by(id=user_id)
                .first()
        )
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

    def get_list(self, user_id: int) -> list[tables.User]:
        users = (self.session.query(tables.User).all())
        return users

    def get(self, user_id: int) -> tables.User:
        return self._get(user_id)

    def create(self, user_data: UserCreate) -> tables.User:
        user = tables.User(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_id: int, user_data: UserUpdate) -> tables.User:
        user = self._get(user_id)
        for field, value in user_data:
            setattr(user, field, value)
        self.session.commit()
        return user

    def delete(self, user_id: int):
        user = self._get(user_id)
        self.session.delete(user)
        self.session.commit()
