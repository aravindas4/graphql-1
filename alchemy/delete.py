from syslog import LOG_LOCAL0
from sqlalchemy.orm import sessionmaker

# from sqlalchemy import desc

from alchemy.base import User, engine


Session = sessionmaker()
local_session = Session(bind=engine)

def delete_user():
    user_to_delete = local_session.query(User).filter(User.username == "correct").first()

    local_session.delete(user_to_delete)

    local_session.commit()

    local_session.rever