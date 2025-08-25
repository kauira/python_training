from model.contact import Contact

def test_edit_contact_form(app):
    app.session.login( username="admin", password="secret")
    app.contact.edit_contact_form(Contact(firstname="new", middlename="new", lastname="new", nickname="new", title="new", company="new", address="new", home="new", mobile="new",
                               work="new", fax="new", email="new", email2="new", email3="new", homepage="new", bday="11", bmonth="October", byear="222",
                               aday="16", amonth="may", ayear="323"))
    app.session.logout()

# def test_delete_contact_on_edit_page(app):
   # app.session.login( username="admin", password="secret")
   # app.contact.edit_delete_contact_on_edit_page(Contact(firstname="ggg", middlename="fgh", lastname="dfg", nickname="rgrgrg", title="dfgd", company="erferfer", address="dfgdgdd", home="dfgdfg", mobile="dgdgdgd",
     #                          work="dgdgdg", fax="dfgdgdf", email="dfgvdfgfd", email2="dfgdgfgd", email3="dgdgd", homepage="dgdgdg", bday="10", bmonth="September", byear="111",
     #                          aday="1111", amonth="August", ayear="15"))
    #app.session.logout()