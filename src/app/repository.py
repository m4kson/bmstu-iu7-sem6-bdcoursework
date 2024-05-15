from sqlalchemy.orm import Session
from typing import List
from schemas import *
from models import *


class DetailRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_detail(self, detail_create: SDetail) -> Detail:
        detail = Detail(
            name=detail_create.name,
            country=detail_create.country,
            amount=detail_create.amount,
            price=detail_create.price,
            length=detail_create.length,
            height=detail_create.height,
            width=detail_create.width
        )
        self.db.add(detail)
        self.db.commit()
        self.db.refresh(detail)
        return detail

    def get_all_details(self, skip: int = 0, limit: int = 10) -> List[Detail]:
        return self.db.query(Detail).offset(skip).limit(limit).all()

