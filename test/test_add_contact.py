# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def ramdom_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix+"".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


def ramdom_numd(prefix, maxlen):
    symbols = string.digits
    return prefix+"".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


testdata = [
    Contact(first_name="", last_name="", address="", phone_m="", phone_home="", phone_work="",
            email="", email2="", email3="")] + \
           [
    Contact(first_name=ramdom_string("name", 10),
            last_name=ramdom_string("last_name", 10),
            address=ramdom_string("address", 10),
            phone_m=ramdom_numd("", 10),
            phone_home=ramdom_numd("", 10),
            phone_work=ramdom_numd("", 10),
            email=ramdom_string("email", 10),
            email2=ramdom_string("email2", 10),
            email3=ramdom_string("email3", 10),
            )
               for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x)for x in testdata])
def test_create_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # добавить контакт в старый список
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
