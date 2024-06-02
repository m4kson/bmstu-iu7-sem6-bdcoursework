from fastapi import FastAPI
import uvicorn
from app.routers import router

from app.auth.schemas import UserCreate, UserRead
from fastapi_users import FastAPIUsers
from auth.auth_user_model import User
from auth.manager import get_user_manager
from auth.auth import auth_backend

app = FastAPI(
    title="ProductMonitor"
)
app.include_router(router)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9877)

