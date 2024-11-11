from model.group import Group


def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first(Group(name="test_up", header="head_up", footer="footer_up"))
    app.session.logout()
