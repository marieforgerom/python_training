# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_new_group(Group(name="fghfhg", header="qerwer", footer="asds"))
    app.session.logout()

