# -*- coding: utf-8 -*-


def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.dell_first()
    app.session.logout()
