import sqlalchemy
from sqlalchemy import create_engine, text
from config import settings
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase, class_mapper
from models import *

def create_session(recreate=False):
    print("Версия SQL Alchemy:", sqlalchemy.__version__)

    engine = create_engine(
        #f'postgresql+psycopg://m4ks0n:admin@localhost:5432/ProductMonitor',
        url=settings.DATABASE_URL_psycopg,
        echo=False,
        pool_pre_ping=True
    )
    
    try:
        engine.connect()
        print("DB succesfully connected")
        # with engine.connect() as conn:
        #     res = conn.execute(text("SELECT VERSION()"))
        #     print("Версия PostgreSQL: {}".format(res.first()[0]))

    except:
        print("Connetion to db failed")
        return

    Session = sessionmaker(bind=engine)
    db = Session()

    if recreate:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    
    return db

def get_db():
    db = create_session()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    create_session(True)

