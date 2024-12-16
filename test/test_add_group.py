# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # сравниваем длинну старого списка с количеством групп на странице
    assert len(old_groups)+1 == app.group.count()
    # если предыдущая проверка успешна - загружаем новый список
    new_groups = app.group.get_group_list()
    # добавить группу в старый список
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


