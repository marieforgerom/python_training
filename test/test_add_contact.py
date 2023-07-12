# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact("etrt", "fghfh", "yuiui", "tyt", "rtet", "cvgfhfh", "dfhdhd", "345565", "234345",
                             "234234", "678899", "wrerwer", "werewr", "werwer", "werrwer", "1", "January", "1989", "2",
                             "March", "1990", "erertry", "fhfgh", "fghfhfg"))
    app.session.logout()

