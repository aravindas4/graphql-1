from alchemy.base import User, engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
local_session = Session(bind=engine)

def display_users():
    users = local_session.query(User).all()

    for user in users:
        print(str(user))

    user = local_session.query(User).filter(User.username=="some").first()

    print(user.email)