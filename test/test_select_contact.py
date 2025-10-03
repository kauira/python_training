from model.contact import Contact
import random

def test_select_contact_by_id(app):
    contact = random.choice(app.contact.get_contact_list())
    app.contact.select_contact_by_id(contact.id)