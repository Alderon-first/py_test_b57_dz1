from model.group import Group
from random import randrange
import random


def test_update_first_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = Group(name="test_up", header="head_up", footer="footer_up")
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.update_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[new_groups.index(group)] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui :
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


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
