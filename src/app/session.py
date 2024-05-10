import sqlalchemy
from sqlalchemy import create_engine, text, URL
from config import settings

def create_connection(recreate=False):
    print("Версия SQL Alchemy:", sqlalchemy.__version__)

    engine = create_engine(
        #f'postgresql+psycopg://m4ks0n:admin@localhost:5432/ProductMonitor',
        url=settings.DATABASE_URL_psycopg,
        echo=True,
    )

    with engine.connect() as conn:
        res = conn.execute(text("SELECT VERSION()"))
        print(f"{res=}")


if __name__ == "__main__":
    create_connection(True)

