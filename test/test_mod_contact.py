from random import randrange
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact("etrt", "fghfh", "yuiui"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact("tttt", "fghfh", "yyyy", "tyt", "rtet", "cvgfhfh", "dfhdhd", "345565", "234345", "234234",
                      "678899", "wrerwer", "werewr", "werwer", "werrwer", "12", "March", "1989", "18", "May", "1990",
                      "erertry", "fhfgh", "hhhhh")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

