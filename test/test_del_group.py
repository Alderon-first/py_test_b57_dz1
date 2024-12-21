# -*- coding: utf-8 -*-
import random

from model.group import Group
from random import randrange
import random


def test_del_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.dell_by_id(group.id)
    assert len(old_groups)-1 == app.group.count()
    new_groups = db.get_group_list()
    # вырезаем элемент c индексом index
    old_groups.remove(group)
    assert old_groups == new_groups
