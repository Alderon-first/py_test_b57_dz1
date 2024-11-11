from model.group import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.update_first(Group(name="test_up", header="head_up", footer="footer_up"))


def test_update_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.update_first(Group(name="test_new"))


def test_update_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.update_first(Group(header="head_new"))
