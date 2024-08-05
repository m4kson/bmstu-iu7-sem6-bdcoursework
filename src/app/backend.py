from fastapi import Depends, FastAPI
import fastapi_users
import uvicorn
from app.auth.auth_user_model import User
from app.routers import router



app = FastAPI(
    title="ProductMonitor"
)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9877)

