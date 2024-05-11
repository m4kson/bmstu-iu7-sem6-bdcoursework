from sqlalchemy import text, insert, bindparam
from session import get_db
from models import *
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

def insert_assemblyline():
    session = next(get_db())
    new_line = AssemblyLine(
        name = 'Line 8',
        length=130,
        height=52,
        width=31,
        status='работает', 
        production=100,
        downtime=10, 
        inspectionsamountperyear=12, 
        lastinspectiondate='2023-01-01',
        nextinspectiondate='2024-01-01',
        defectrate=2
    )
    session.add(new_line)
    session.commit()

insert_assemblyline()