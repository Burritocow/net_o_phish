from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
engine = create_engine('mysql+pymysql://phish:2fEXKAqkA9Bn@localhost/test_db', echo=False)
Session.configure(bind=engine)

session = Session()
