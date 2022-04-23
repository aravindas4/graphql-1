import os
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, create_engine

from datetime import datetime

Base = declarative_base()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = "sqlite:///" + os.path.join(BASE_DIR, "site.db")

engine = create_engine(connection_str, echo=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), unique=True, nullable=True)
    date_created = Column(DateTime(), default=datetime.utcnow)


    def __str__(self) -> str:
        return f"<User username={self.username}>"