from typing import Annotated
from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from session import get_db
from models import *
from schemas import *
from repository import *
import uvicorn

app = FastAPI()


# tarctors
@app.post("/tractors/", response_model=STractor)
def create_tractor(
    tractor_create: Annotated[STractor, Depends()],
    db: Annotated[Session, Depends(get_db)]
):
    tractor_repo = TractorRepository(db)
    return tractor_repo.add_tractor(tractor_create)

@app.get("/tractors/", response_model=List[STractor])
def read_tractors(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 10,
):
    tractor_repo = TractorRepository(db)
    return tractor_repo.get_all_tractors(skip=skip, limit=limit)

#details
@app.post("/details/", response_model=SDetail)
def create_detail(
    detail_create: Annotated[SDetail, Depends()], 
    db: Annotated[Session, Depends(get_db)]
):
    detail_repo = DetailRepository(db)
    return detail_repo.add_detail(detail_create)

@app.get("/details/", response_model=List[SDetail])
def read_details(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 10,
):
    detail_repo = DetailRepository(db)
    return detail_repo.get_all_details(skip=skip, limit=limit)

#assemblylines
@app.post("/lines/", response_model=SAssemblyLine)
def create_line(
    line_create: Annotated[SAssemblyLine, Depends()], 
    db: Annotated[Session, Depends(get_db)]
):
    line_repo = AssemblyLineRepository(db)
    return line_repo.add_assembly_line(line_create)

@app.get("/lines/", response_model=List[SAssemblyLine])
def read_lines(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 10,
):
    line_repo = AssemblyLineRepository(db)
    return line_repo.get_all_assembly_lines(skip=skip, limit=limit)

#users
@app.post("/users/", response_model=SUser)
def create_user(
    user_create: Annotated[SUser, Depends()], 
    db: Annotated[Session, Depends(get_db)]
):
    user_repo = UserRepository(db)
    return user_repo.add_user(user_create)

@app.get("/users/", response_model=List[SUser])
def read_users(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 10,
):
    user_repo = UserRepository(db)
    return user_repo.get_all_users(skip=skip, limit=limit)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9877)

