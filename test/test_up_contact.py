# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
    app.contact.update_first(Contact(first_name="Вельгельмина", last_name="Христорождественская",
                                     address="Новосиб, д.13", phone_m="+7-977-89-96-13", email="test11@test11.ru"))


def test_update_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
    app.contact.update_first(Contact(first_name="Капитолина"))
