from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="ggg", middlename="fgh", lastname="dfg", nickname="rgrgrg", title="dfgd", company="erferfer", address="dfgdgdd", home="dfgdfg", mobile="dgdgdgd",
                               work="dgdgdg", fax="dfgdgdf", email="dfgvdfgfd", email2="dfgdgfgd", email3="dgdgd", homepage="dgdgdg", bday="10", bmonth="September", byear="111",
                               aday="15", amonth="August", ayear="1111"))
    app.session.logout()


