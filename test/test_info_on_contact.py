import re
from random import randrange
from model.contact import Contact


def test_rand_phones_on_home_page(app):
    count_contact = app.contact.get_contact_list()
    index = randrange(len(count_contact))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_rand_phones_on_contact_view_page(app):
    count_contact = app.contact.get_contact_list()
    index = randrange(len(count_contact))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert merge_phones_like_on_home_page(contact_from_edit_page) == \
           merge_phones_like_on_home_page(contact_from_view_page)


def test_contact_info_on_home_page(app):
    count_contact = app.contact.get_contact_list()
    index = randrange(len(count_contact))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


def test_contact_info_on_home_page_db(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for contact_home, contact_db in zip(contact_from_home_page, contact_from_db):
        assert contact_home.first_name == contact_db.first_name
        assert contact_home.last_name == contact_db.last_name
        assert contact_home.address == contact_db.address
        assert contact_home.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)
        assert contact_home.all_emails_from_home_page == merge_email_like_on_home_page(contact_db)
    assert contact_from_home_page == contact_from_db


def clear(s):
    # метод удаления лишних символов из строки
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    # список телефонов контакта фильтруется по None
    # к отфильтрованному списку применяется очистка
    # к очищенному списку применяется фильтр, отбрасываются пустые
    # оставшиеся элементы склеиваются с разделителем \n
    # здесь нет phone2!!!!! - не могу создать -> не могу найти на странице просмотра
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                                           [contact.phone_home, contact.phone_m, contact.phone_work]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email, contact.email2, contact.email3])))


