# -*- coding: utf-8 -*-
from мodel.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test_g", header="head", footer="footer"))
    app.session.logout()


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


    