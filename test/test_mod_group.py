from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="uuuuu", header="oooooo", footer="aaaaaa"))
    app.session.logout()