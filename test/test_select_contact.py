from model.contact import Contact


def test_select_contact_by_id(app):
    app.contact.edit_contact_by_id(Contact(firstname="test"))