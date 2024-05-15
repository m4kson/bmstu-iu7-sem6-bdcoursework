from typing import Annotated
from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from session import get_db
from models import *
from schemas import *
from repository import *
import uvicorn

app = FastAPI()


#select

@app.get("/tractors")
def get_all_tractors(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    tractors = db.query(Tractor).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(tractors), 'details': tractors}

@app.get("/assembly_lines")
def get_all_assembly_lines(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    lines = db.query(AssemblyLine).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(lines), 'details': lines}

@app.get("/service_requests")
def get_all_service_requests(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    requests = db.query(ServiceRequest).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(requests), 'details': requests}

@app.get("/service_reports")
def get_all_service_reports(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    reports = db.query(ServiceReport).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(reports), 'details': reports}

@app.get("/users")
def get_all_users(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    users = db.query(User).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(users), 'details': users}

@app.get("/Orders")
def get_all_orders(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    orders = db.query(DetailOrder).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(orders), 'details': orders}


@app.get("/details")
def get_all_details(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    details = db.query(Detail).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(details), 'details': details}


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



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9877)

