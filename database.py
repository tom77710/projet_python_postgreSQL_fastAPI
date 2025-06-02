from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/DungeonsAndDragons"

# DEF ENGINE
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# DEF OF SESSION
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# DEF OF BASE AS AN OBJECT TO USE
Base = declarative_base()

# DEPENDENCY CORE
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# DEPENDENCY ANNOTATED
db_dependency = Annotated[Session, Depends(get_db)]