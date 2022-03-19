from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_URL = "sqlite:///database.db"

engine = create_engine(
    SQL_ALCHEMY_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit= False, bind = engine)

Base = declarative_base()