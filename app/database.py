from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config.config import settings

# print('"""""""""""""""""""""""')
# print(settings.postgres_user)
# print(settings.postgres_password)
# print(settings.postgres_db)
# print('"""""""""""""""""""""""')

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}/{settings.postgres_db}"
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://admin:password@localhost:5432/fast-api-db2"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
