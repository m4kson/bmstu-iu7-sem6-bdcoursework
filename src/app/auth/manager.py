from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from app.auth.auth_user_model import User, get_user_db
from app.auth.schemas import UserAdd, UserCreate, UserRead

SECRET = "SECRET"


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def create(self, user_create: UserCreate, safe: bool = False, request: Optional[Request] = None) -> User:
        # Создаем словарь данных для создания пользователя
        new_user = {
            "name": user_create.name,
            "surname": user_create.surname,
            "fathername": user_create.fathername,
            "email": user_create.email,
            "sex": user_create.sex,
            "password": user_create.password,
            "role": "на верификации",
            "department": user_create.department,
            "dateofbirth": user_create.dateofbirth,
            "is_active": True,
            "is_superuser": False,
            "is_verified": False
        }

        # Создаем пользователя с обновленными данными
        created_user = await super().create(user_create=UserAdd(**new_user), safe=safe, request=request)

        return created_user

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


