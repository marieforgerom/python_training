from model.group import Group


def test_mod_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="uuuuu", header="oooooo", footer="aaaaaa"))