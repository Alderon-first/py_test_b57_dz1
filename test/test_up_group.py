from model.group import Group


def test_update_first_group(app):
    app.group.update_first(Group(name="test_up", header="head_up", footer="footer_up"))


def test_update_first_group_name(app):
    app.group.update_first(Group(name="test_new"))


def test_update_first_group_header(app):
    app.group.update_first(Group(header="head_new"))
