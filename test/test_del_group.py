def test_dell_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.dell_first()
    app.session.logout()
