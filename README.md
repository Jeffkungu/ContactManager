# ContactManager
##A console application for contact management and sending SMS

###Installation
$ git clone https://github.com/Jeffkungu/bc-15-contact-manager.git
$ cd bc-15-contact-manager

###Create and activate a virtual environment.
$ virtualenv .env
$ source .env/bin/activate

###Install dependencies
$ pip install -r requirements.txt

###Run the app
python app.py -i

###Commands
app.py (-i | --interactive)
app.py (-h | --help )
app.py (-v | --version)
$: add -f <first_name> -l <last_name> -p <phone_number>
$: search
$: send <first_name> 
$: help

