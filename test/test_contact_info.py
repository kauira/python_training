import re
from random import randrange

from model.contact import Contact


def test_contact_info_on_homepage(app,db):
    contacts_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for contact in contacts_from_homepage:
        index = contacts_from_homepage.index(contact)
        assert contact.lastname == contacts_from_db[index].lastname
        assert contact.firstname == contacts_from_db[index].firstname
        assert contact.address == contacts_from_db[index].address
        assert contact.all_phones_from_homepage == contacts_from_db[index].all_phones_from_db
        assert contact.all_emails_from_homepage == contacts_from_db[index].all_emails_from_homepage

def test_phones_on_contact_view_page(app, db):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home, contact.work, contact.mobile]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,[contact.email, contact.email2, contact.email3])))

