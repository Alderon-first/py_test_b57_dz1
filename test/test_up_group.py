from model.group import Group
from random import randrange
import random


def test_update_first_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = Group(name="test_up", header="head_up", footer="footer_up")
    # добавили в объект group old_groups[0].id - id изменяемой группы. 0 потому, что тест "изменение первой группы"
    group_id = (random.choice(old_groups)).id
    app.group.update_by_id(group_id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_update_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     app.group.update_first(Group(name="test_new"))
#
#
# def test_update_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     app.group.update_first(Group(header="head_new"))
