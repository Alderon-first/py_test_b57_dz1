from model.contact import Contact
import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    print(contact_from_edit_page)
    assert contact_from_home_page.phone_home == clear(contact_from_edit_page.phone_home)
    assert contact_from_home_page.phone_work == clear(contact_from_edit_page.phone_work)
    assert contact_from_home_page.phone_m == clear(contact_from_edit_page.phone_m)
    # assert contact_from_home_page.phone_second == contact_from_edit_page.phone_second


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    print("contact_from_view_page.[0]")
    print(contact_from_view_page.phone_home)
    print(contact_from_view_page.phone_m)
    print(contact_from_view_page.phone_work)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    print(contact_from_edit_page)
    assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
    assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work
    assert contact_from_view_page.phone_m == contact_from_edit_page.phone_m
    # assert contact_from_home_page.phone_second == contact_from_edit_page.phone_second


def clear(s):
    # метод удаления лишних символов из строки
    return re.sub("[() -]]", "", s)


# здесь нет phone2!!!!!
