# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact("etrt", "fghfh", "yuiui", "tyt", "rtet", "cvgfhfh", "dfhdhd", "345565", "234345",
                             "234234", "678899", "wrerwer", "werewr", "werwer", "werrwer", "1", "January", "1989", "2",
                             "March", "1990", "erertry", "fhfgh", "fghfhfg"))
    app.session.logout()

