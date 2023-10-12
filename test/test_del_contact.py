from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact("etrt", "fghfh", "yuiui", "tyt", "rtet", "cvgfhfh", "dfhdhd", "345565", "234345",
                             "234234", "678899", "wrerwer", "werewr", "werwer", "werrwer", "1", "January", "1989", "2",
                             "March", "1990", "erertry", "fhfgh", "fghfhfg"))
    app.contact.delete_first_contact()
