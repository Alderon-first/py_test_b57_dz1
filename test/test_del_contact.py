# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="ДлинноеТестовоеИмя"))
    old_contacts = app.contact.get_contact_list()
    # получить значение индекса случайным образом из диапазона, равного длинне списка
    index = randrange(len(old_contacts))
    app.contact.dell_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    #  вырезаем элемент c индексом index
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
