# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    # загружаем список из базы
    app.group.create(group)
    # если предыдущая проверка успешна - загружаем новый список из базы
    new_groups = db.get_group_list()
    # добавить группу в старый список
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


