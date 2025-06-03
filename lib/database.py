from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base  


engine = create_engine('sqlite:///lib/livestock.db')

Session = sessionmaker(bind=engine)

session = Session()

Base.metadata.create_all(engine)
