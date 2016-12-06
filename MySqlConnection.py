from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import yaml

def generateConnectionString():
    props = yaml.load(open('config/config.yaml', 'r'))
    props = props['mysql']
    connectionString = '{}+{}://{}:{}@localhost/{}'.format(props['dialect'], props['driver'], props['user'], props['password'], props['database'])

    return connectionString

Session = sessionmaker()
engine = create_engine(generateConnectionString(), echo=False)
Session.configure(bind=engine)

session = Session()