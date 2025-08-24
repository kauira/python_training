# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.contant import Contant

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contant(firstname="ggg", middlename="fgh",lastname="dfg", nickname="rgrgrg", title="dfgd", company="erferfer", address="dfgdgdd", home="dfgdfg", mobile="dgdgdgd",
                                work="dgdgdg", fax="dfgdgdf", email="dfgvdfgfd", email2="dfgdgfgd", email3="dgdgd", homepage="dgdgdg", bday="10", bmonth="September", byear="111",
                            aday="1111", amonth="August", ayear="15"))
    app.session.logout()


