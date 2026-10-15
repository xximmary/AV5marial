
from sqlalchemy import create_engine
#importamos do arquivo classes a Base
from classes import Base, engine 
#imports pro mysql
import os
from dotenv import load_dotenv


def conectar_sqlite():
    Base.metadata.create_all(engine)

    return engine

def conectar_mysql():
    load_dotenv()

    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    )

    Base.metadata.create_all(engine)

    return engine