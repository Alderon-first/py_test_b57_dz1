# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random


def test_update_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
    old_contacts = db.get_contact_list()
    contact = Contact(first_name="Вельгельмина", last_name="Христорождественская",
                      address="Новосиб, д.13", phone_m="+7-977-89-96-13")
    contact_id = (random.choice(old_contacts)).id
    app.contact.update_by_id(contact_id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[new_contacts.index(contact)] = contact
    assert old_contacts == new_contacts
    # if check_ui :
    #     assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
    #                                                                  key=Contact.id_or_max)

# def test_update_contact_first_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
#     app.contact.update_first(Contact(first_name="Капитолина"))
