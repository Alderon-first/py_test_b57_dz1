# -*- coding: utf-8 -*-
from мodel.contact import Contact


def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Katerina", last_name="Ushko", address="MSK, Lasareva, 66-66",
                               phone_m="8-977-89-96-13", email="test@test.ru"))
    app.session.logout()

