from models import Base, User, session


def addperson(fname, lname, phonenum):

    if (fname and lname) and phonenum:
        if type(fname) is str and type(lname) is str:
            if type(phonenum) is str:    
                
                contact = session.query(User).filter_by(phoneno=phonenum).all()
                if not contact:
                    
                    new_user = User(fname=fname, lname=lname, phoneno=phonenum)
                    session.add(new_user)
                    session.commit()
                    print("User added")
                else:
                    print("Contact already exists")
            else:
                print("Phone number should be numbers")
        else:
            print("Names should be letters")
    else:
        print("Variables should not be blank")

addperson("Sam", "Kungu", "0717551051")
