from .base import User, engine, Base

def create():
    Base.metadata.create_all(engine)