import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:///C:\\Users\\Jeff\\Desktop\\ContactManager\\Contacts.sqlite', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    phoneno = Column(String)

    def __init__(self, fname, lname, phoneno):
        self.fname = fname
        self.lname = lname
        self.phoneno = phoneno

Base.metadata.create_all(engine)

