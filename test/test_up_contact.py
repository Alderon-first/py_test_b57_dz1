# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first(Contact(first_name="Вельгельмина", last_name="Христорождественская",
                                     address="Новосиб, д.13", phone_m="+7-977-89-96-13", email="test11@test11.ru"))
    app.session.logout()


def test_update_contact_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first(Contact(first_name="Капитолина"))
    app.session.logout()
