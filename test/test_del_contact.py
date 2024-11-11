# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
    app.contact.dell_first()

