from sqlalchemy.orm import sessionmaker

from alchemy.base import engine, User

Session = sessionmaker()
local_session = Session(bind=engine)

def update_user():
    user_to_update = local_session.query(User).filter(User.username=="some").first()

    user_to_update.username = "correct"
    user_to_update.email = "correct@email.com"

    local_session.commit()

    print(user_to_update.username)


    