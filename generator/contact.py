from model.contact import Contact
import random
import string
import getopt
import jsonpickle
import os.path
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_srting(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(lastname="", firstname="", address="", home="", work="", mobile="", email="", email2="", email3="")] + [
    Contact(lastname = random_srting("lastname", 10), firstname=random_srting("firstname", 20),
            address = random_srting("address", 20), home=random_srting("home", 20), work=random_srting("work", 10),
            mobile=random_srting("mobile", 10), email=random_srting("email", 20), email2=random_srting("email2", 20),
            email3=random_srting("email3", 20))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))