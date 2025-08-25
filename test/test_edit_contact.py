from model.contact import Contact

def test_edit_contact_form(app):
    app.session.login( username="admin", password="secret")
    app.contact.edit_contact_form(Contact(firstname="new", middlename="new", lastname="new", nickname="new", title="new", company="new", address="new", home="new", mobile="new",
                               work="new", fax="new", email="new", email2="new", email3="new", homepage="new", bday="11", bmonth="October", byear="222",
                               aday="16", amonth="may", ayear="323"))
    app.session.logout()

