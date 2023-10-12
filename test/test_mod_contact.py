from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact("etrt", "fghfh", "yuiui", "tyt", "rtet", "cvgfhfh", "dfhdhd", "345565", "234345",
                             "234234", "678899", "wrerwer", "werewr", "werwer", "werrwer", "1", "January", "1989", "2",
                             "March", "1990", "erertry", "fhfgh", "fghfhfg"))
    app.contact.modify_first_contact(Contact("tttt", "fghfh", "yyyy", "tyt", "rtet", "cvgfhfh", "dfhdhd", "345565", "234345",
                                             "234234", "678899", "wrerwer", "werewr", "werwer", "werrwer", "12",
                                             "March", "1989", "18", "May", "1990", "erertry", "fhfgh", "hhhhh"))
