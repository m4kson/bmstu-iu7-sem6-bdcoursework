import sqlalchemy
from sqlalchemy import create_engine, text, URL
from config import settings
from sqlalchemy.orm import Session, sessionmaker

def create_session(recreate=False):
    print("Версия SQL Alchemy:", sqlalchemy.__version__)

    engine = create_engine(
        #f'postgresql+psycopg://m4ks0n:admin@localhost:5432/ProductMonitor',
        url=settings.DATABASE_URL_psycopg,
        echo=False,
    )

    with engine.connect() as conn:
        res = conn.execute(text("SELECT * from assemblylines"))
        print(f"{res.first()=}")

if __name__ == "__main__":
    create_session(True)

