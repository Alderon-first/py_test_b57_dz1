# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random


def test_del_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
    old_contacts = db.get_contact_list()
    # получить значение индекса случайным образом из диапазона, равного длинне списка
    contact = random.choice(old_contacts)
    app.contact.dell_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
