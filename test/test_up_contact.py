# -*- coding: utf-8 -*-
from model.contact import Contact


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Вельгельмина", last_name="Христорождественская",
                                     address="Новосиб, д.13", phone_m="+7-977-89-96-13", email="test11@test11.ru")
    contact.id = old_contacts[0].id
    app.contact.update_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_update_contact_first_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
#     app.contact.update_first(Contact(first_name="Капитолина"))
