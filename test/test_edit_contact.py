from model.contact import Contact
import random

def test_some_contact_form(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    new_contact = Contact(lastname="test", firstname="test")
    new_contact.id = contact.id
    app.contact.edit_contact_by_id(new_contact.id, new_contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



