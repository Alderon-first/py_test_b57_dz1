# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Katerina", last_name="Ushko", address="MSK, Lasareva, 66-66",
                      phone_home="+029 329 8482347", phone_m="2-222-22-22", phone_work='3(333)333333333', email="test@test.ru")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # добавить контакт в старый список
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
