from model.group import Group
from random import randrange


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="test_up", header="head_up", footer="footer_up")
    # добавили в объект group old_groups[0].id - id изменяемой группы. 0 потому, что тест "изменение первой группы"
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.update_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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
