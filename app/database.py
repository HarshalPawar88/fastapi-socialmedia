import time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote

from app.config import settings
from . import models
from psycopg2.extras import RealDictCursor

#SQLALCHEMY_DATABASE_URL= 'postgresql://<username>:<password>@<ip-address/hostname>/database_name'

SQLALCHEMY_DATABASE_URL= f"postgresql://{settings.database_username}:%s@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine=create_engine(SQLALCHEMY_DATABASE_URL % quote(settings.database_password))
SessionLocal= sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base= declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# while True:
#     try:
#         conn= psycopg2.connect(host='localhost',database='fastapi',
#         user='postgres',password='hpawar@123', cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Database Connection was Succesful");
#         break

#     except Exception as error:
#         print("Connection to database failed")
#         print("Error", error)
#         time.sleep(2)