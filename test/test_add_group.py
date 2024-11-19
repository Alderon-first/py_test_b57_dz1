# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string


def ramdom_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits+string.punctuation+' '*10
    return prefix+"".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


testdata = [
    Group(name="", header="", footer="")] + \
           [
    Group(name=ramdom_string("name", 10), header=ramdom_string("header", 20), footer=ramdom_string("footer", 20))
               for i in range(5)
]
# вариант тестдаты с перебором комбинаций
# testdata = [
#     Group(name="name", header=header, footer=footer)
#     for name in ["", ramdom_string("name", 10)]
#     for header in ["", ramdom_string("header", 20)]
#     for footer in ["", ramdom_string("footer", 20)]
# ]


@pytest.mark.parametrize("group", testdata, ids=[str(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # сравниваем длинну старого списка с количеством групп на странице
    assert len(old_groups)+1 == app.group.count()
    # если предыдущая проверка успешна - загружаем новый список
    new_groups = app.group.get_group_list()
    # добавить группу в старый список
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


