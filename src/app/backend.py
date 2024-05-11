from fastapi import FastAPI, Depends, HTTPException, status, APIRouter, Response
from models import *
#todo import schemas
from session import create_session, get_db
import uvicorn
from sqlalchemy.orm import Session
import time

app = FastAPI()


@app.get("/home")
def get_home():
    return "hello, world!"

@app.get("/details_read")
def get_all_details(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 2) * limit
    details = db.query(Detail).limit(limit).offset(skip).all()
    return {'status' : 'success', 'results': len(details), 'details' : details}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9877)