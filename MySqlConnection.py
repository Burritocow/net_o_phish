from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
# TODO for the love of god don't publish this thing below (find way to not hardcode password)
Session.configure(bind=engine)

session = Session()