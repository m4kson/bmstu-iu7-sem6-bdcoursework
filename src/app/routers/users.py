# from enum import Enum
# from typing import Annotated
# from fastapi import APIRouter, Depends, HTTPException, status
# from app.auth.auth_user_model import User
# from app.auth.manager import get_user_manager
# from app.auth.schemas import UserCreate, UserRead
# from auth.auth import auth_backend
# import fastapi_users
# from fastapi_users import FastAPIUsers

# class Role(str, Enum):
#     ADMIN = "администратор"
#     OPERATOR = "оператор производства"
#     SPECIALIST = "специалист по обслуживанию"

# fastapi_users = FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )

# current_user = fastapi_users.current_user()


# async def get_user(user: User = Depends(fastapi_users.current_user())) -> User:
#     return user

# def get_admin_user(user: Annotated[User, Depends(get_user)]) -> User:
#     if user.role != Role.ADMIN:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this resource"
#         )
#     return user

# def get_operator_user(user: Annotated[User, Depends(get_user)]) -> User:
#     if user.role != Role.OPERATOR:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this resource"
#         )
#     return user

# def get_specialist_user(user: Annotated[User, Depends(get_user)]) -> User:
#     if user.role != Role.SPECIALIST:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this resource"
#         )
#     return user


# router_auth = APIRouter(
#     prefix="/auth/jwt",
#     tags=["Auth"]
# )

# @router_auth.post("")
# async def auth_router():
#     fastapi_users.get_auth_router(auth_backend),

# @router_auth.post("reg/")
# async def register_router():
#     fastapi_users.get_register_router(UserRead, UserCreate),


# @router_auth.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.name}"

# @router_auth.get("/protected-route-for-admin")
# def protected_route(user: User = Depends(get_admin_user)):
#     return f"Hello, {user.email}. Your role is {user.role}"

# @router_auth.get("/protected-route-for-operator")
# def protected_route(user: User = Depends(get_operator_user)):
#     return f"Hello, {user.email}. Your role is {user.role}"

# @router_auth.get("/protected-route-for-specialist")
# def protected_route(user: User = Depends(get_specialist_user)):
#     return f"Hello, {user.email}. Your role is {user.role}"

# @router_auth.get("/unprotected-route")
# def unprotected_route():
#     return f"Hello, anonym"