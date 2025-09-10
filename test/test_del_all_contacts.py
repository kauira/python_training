from model.contact import Contact

def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_all_contacts()
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == 0
    old_contacts = []
    assert old_contacts == new_contacts
