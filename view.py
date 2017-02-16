import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User


def view():
	print("Contacts: ")
	print(tabulate(View, headers=['first_name', 'last_name', 'pnum'])

view ("Jeff")			
