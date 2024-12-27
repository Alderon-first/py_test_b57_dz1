# -*- coding: utf-8 -*-
import random

from model.group import Group
from random import randrange
import random


def test_del_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.dell_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=group.id_or_max()) == sorted(app.group.get_group_list(), key=group.id_or_max())
