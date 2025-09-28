from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

# Base Class for creating Tables
class Base(DeclarativeBase):
  pass

# Database URL
DB_URL= f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# Database Engine
engine = create_engine(DB_URL, echo=True)

# Database Session Creation
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Dependency 
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()