import random
from model.contact import Contact
from fixture.orm import ORMFixture

db = ORMFixture(host='127.0.0.1',name='addressbook',user='root',password='')

def test_add_contact_to_group(app):
    contacts = app.contact.get_contact_list()
    groups = app.group.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    group_contacts = app.contact.get_contacts_in_group(group.id)
    if contact in group_contacts:
        app.contact.remove_contact_from_group(contact.id, group.id, group.name)
    app.contact.add_contact_to_group(contact.id,group.id)
    assert sorted(group_contacts, key=Contact.id_or_max) == sorted(db.get_contacts_in_group(group), key=Contact.id_or_max)

def test_remove_contact_from_group(app):
    contacts = app.contact.get_contact_list()
    contact = random.choice(contacts)
    groups = db.get_group_list()
    group = random.choice(groups)
    group_contacts = app.contact.get_contacts_in_group(group.id)
    if contact not in group_contacts:
        app.contact.add_contact_to_group(contact.id,group.id)
    app.contact.remove_contact_from_group(contact.id,group.id, group.name)
    assert contact in db.get_contacts_not_in_group(group)



