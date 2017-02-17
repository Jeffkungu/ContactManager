from models import Base, User, session
from tabulate import tabulate


def search(first_name):
	users = session.query(User).filter(User.fname.like('%' + first_name + '%')).all()
	if not users:
		return "User not found"

	for user in users:
		print(str(user.id))
		print(user.fname)
		print(user.lname)
		print(user.phoneno)
        user_data = [str(user.id), user.fname, user.lname, user.phoneno]

	return tabulate([user_data], headers=['Id', 'first_name', 'last_name', 'pnum'])