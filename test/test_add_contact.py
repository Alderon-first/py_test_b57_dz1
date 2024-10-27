# -*- coding: utf-8 -*-
from мodel.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="Katerina", last_name="Ushko", address= "MSK, Lasareva, 66-66",
                                    phone_m="8-977-89-96-13", email="test@test.ru"))
    app.session.logout()

