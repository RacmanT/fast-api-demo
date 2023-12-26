from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config.config import settings

db_user = settings.model_config.get('POSTGRES_USER')
db_password = settings.model_config.get('POSTGRES_PASSWORD')
db_name = settings.model_config.get('POSTGRES_DB')

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://${db_user}:${db_password}@localhost/${db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
