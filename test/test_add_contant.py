from model.contact import Contact
import random
import string
import pytest

def random_srting(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(lastname="", firstname="", address="", home="", work="", mobile="", email="", email2="", email3="")] + [
    Contact(lastname = random_srting("lastname", 10), firstname=random_srting("firstname", 20),
            address = random_srting("address", 20), home=random_srting("home", 20), work=random_srting("work", 10),
            mobile=random_srting("mobile", 10), email=random_srting("email", 20), email2=random_srting("email2", 20),
            email3=random_srting("email3", 20))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


