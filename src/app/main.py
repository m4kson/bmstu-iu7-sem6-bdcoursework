from sqlalchemy import text, insert, bindparam
from session import sessionfactory
from models import Detail
import uuid

def inseert_data():
    with sessionfactory() as session:
        new_detail = Detail(
            id=uuid.uuid4(),
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