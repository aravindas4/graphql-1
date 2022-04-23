from alchemy.base import User, engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker()



def create_users():
    local_session = Session(bind=engine)
    new_user = User(
        username="some",email="seome@example.com"
    )
    local_session.add(new_user)
    local_session.commit()