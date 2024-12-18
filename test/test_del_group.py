# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_del_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    # получить значение индекса случайным образом из диапазона, равного длине списка
    index = randrange(len(old_groups))
    app.group.dell_by_index(index)
    assert len(old_groups)-1 == app.group.count()
    new_groups = app.group.get_group_list()
    # вырезаем элемент c индексом index
    old_groups[index:index+1] = []
    assert old_groups == new_groups
