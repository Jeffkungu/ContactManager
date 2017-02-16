import sqlalchemy
from models import Base, User, session
from africastalking.AfricasTalkingGateway import (
    AfricasTalkingGateway, AfricasTalkingGatewayException)
# Create specific log in details
username = "Jeffkungu"
apikey = "d37abe476848a7919fe7c5098df7368d9ea3fbcdd14f3c249875f1d05f086ecf"

# Specify the numbers that you want to send text


def send(phonenum):

    user = session.query(User).filter_by(phoneno=phonenum).first()

    if not user:
        print 'User not Found'
        return

    print "Enter message"
    text = raw_input("___")
    message = text.encode('utf8')

    gateway = AfricasTalkingGateway(username, apikey)

    try:

        results = gateway.sendMessage(user.phoneno, message)

        for recipient in results:

            print ("Number: " + recipient['number'] +
                   " Status: " + recipient['status'])

    except AfricasTalkingGatewayException as e:

        print ('Encountered an error while sending: %s' % str(e))


