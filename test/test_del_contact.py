# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
    old_contacts = app.contact.get_contact_list()
    app.contact.dell_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    # вырезаем элемент 0
    old_contacts[0 :1] = []
    assert old_contacts == new_contacts

