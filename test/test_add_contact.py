# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(Contact("etrt", "fghfh", "yuiui", "tyt", "rtet", "cvgfhfh", "dfhdhd", "345565", "234345",
                             "234234", "678899", "wrerwer", "werewr", "werwer", "werrwer", "1", "January", "1989", "2",
                             "March", "1990", "erertry", "fhfgh", "fghfhfg"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

