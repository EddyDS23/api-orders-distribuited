
from app.core.settings import get_settings

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

settings = get_settings()

class Base(DeclarativeBase):
    pass

engine  = create_engine(
    settings.URL_DATABASE,
    pool_size=8,
    max_overflow=4,
    pool_timeout=20,
    pool_recycle=1800,
    pool_pre_ping=True,
    pool_use_lifo=True,
)

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

def get_db():
    db:Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


    