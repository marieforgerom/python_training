from model.group import Group


def test_mod_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="uuuuu", header="oooooo", footer="aaaaaa"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
