# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random


def test_del_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
    old_contacts = db.get_contact_list()
    # получить значение индекса случайным образом из диапазона, равного длинне списка
    contact = random.choice(old_contacts)
    app.contact.dell_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui :
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
