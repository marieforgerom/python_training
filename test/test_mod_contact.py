from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact("tttt", "fghfh", "yyyy", "tyt", "rtet", "cvgfhfh", "dfhdhd", "345565", "234345",
                                             "234234", "678899", "wrerwer", "werewr", "werwer", "werrwer", "12",
                                             "March", "1989", "18", "May", "1990", "erertry", "fhfgh", "hhhhh"))
    app.session.logout()
