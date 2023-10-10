from model.group import Group


def test_add_group(app):
    app.group.modify_first_group(Group(name="uuuuu", header="oooooo", footer="aaaaaa"))