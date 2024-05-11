from sqlalchemy import text, insert, bindparam
from session import get_db
from models import Detail
import uuid

def inseert_data():
    session = next(get_db())
    new_detail = Detail(
        name="Шпендель гк-50",
        country="Китай",
        amount=250,
        price=1.334,
        length=150,
        width=80,
        height=150
    )
    session.add(new_detail)
    session.commit()


inseert_data()