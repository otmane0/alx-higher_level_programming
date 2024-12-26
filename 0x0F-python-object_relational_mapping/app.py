from sqlalchemy.orm import sessionmaker
from model_state import User, engine
from sys import argv



Session = sessionmaker(bind=engine)

session = Session()


users = session.query(User).filter_by(name = "toto").all()

for user in users:

    session.delete(user)

session.commit()

