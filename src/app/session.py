import sqlalchemy
from sqlalchemy import create_engine, text
from config import settings
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from models import Base

def create_session(recreate=False):
    print("Версия SQL Alchemy:", sqlalchemy.__version__)

    engine = create_engine(
        url=settings.DATABASE_URL_psycopg,
        echo=False,
    )
    
    try:
        with engine.connect() as conn:
            res = conn.execute(text("SELECT VERSION()"))
            print("Версия PostgreSQL: {}".format(res.first()[0]))

    except:
        print("Connetion to db failed")

    session_factory = sessionmaker(engine)
    db = Session()

    if recreate:
        Base.metadata.create_all(engine)
    
    return db

def get_db():
    db = create_session()
    try:
        yield db
    
    finally:
        db.close()


