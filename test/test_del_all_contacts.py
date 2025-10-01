from model.contact import Contact

def test_delete_all_contacts(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    app.contact.delete_all_contacts()
    new_contacts = db.get_contact_list()
    old_contacts = []
    assert old_contacts == new_contacts
    if check_ui:
        assert new_contacts == app.contact.get_contact_list()
