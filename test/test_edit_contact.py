from model.contact import Contact

def test_edit_contact_form(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.edit_contact_form(Contact(firstname="new"))


