from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_URL = f"postgresql://{os.getenv('DB_USER', '')}:{os.getenv('DB_PASS', '')}@{os.getenv('DB_HOST', '')}/{os.getenv('DB_NAME', '')}"

engine = create_engine(
    POSTGRES_URL, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
