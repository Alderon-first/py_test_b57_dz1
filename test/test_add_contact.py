# -*- coding: utf-8 -*-
from data.add_contact import testdata
from model.contact import Contact
import pytest


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # добавить контакт в старый список
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
