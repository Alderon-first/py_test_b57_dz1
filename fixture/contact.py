from model.contact import Contact
import re


class ContactHelper:
    # класс ContactHelper предназначен операций с сущностью "контакт": методов создания, удаления и тд
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init group creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit group form
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        # fill group form
        wd = self.app.wd
        self.up_field_value("firstname", contact.first_name)
        self.up_field_value("lastname", contact.last_name)
        self.up_field_value("address", contact.address)
        wd.find_element_by_name("home").click()
        self.up_field_value("mobile", contact.phone_m)
        self.up_field_value("home", contact.phone_home)
        self.up_field_value("work", contact.phone_work)
        self.up_field_value("phone2", contact.phone_second)
        self.up_field_value("email", contact.email)

    def up_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def dell_first(self):
        self.dell_by_index(0)

    def dell_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # выбрать index
        self.select_by_index(index)
        # удалить первую группу
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        self.contact_cache = None

    def update_first(self, contact):
        self.update_by_index(0, contact)

    def update_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        # изменить выбранную
        self.open_edit_page_by_index(index)
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_wiev_page_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("entry")[index].find_elements_by_tag_name("td")[6].\
            find_element_by_tag_name("a").click()

    def open_edit_page_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("entry")[index].find_elements_by_tag_name("td")[7].\
            find_element_by_tag_name("a").click()

    def select_first(self):
        self.select_by_index(0)

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=firstname, last_name=lastname,
                                                  id=id, all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_page_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone_m = wd.find_element_by_name("mobile").get_attribute("value")
        # phone_second = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").text.strip()
        email = wd.find_element_by_name("email").get_attribute('value')
        email2 = wd.find_element_by_name("email2").get_attribute('value')
        email3 = wd.find_element_by_name("email3").get_attribute('value')
        return Contact(first_name=firstname, last_name=lastname,  id=id,
                       phone_m=phone_m, phone_home=phone_home, phone_work=phone_work,
                       address=address,
                       email=email, email2=email2, email3=email3)
        # здесь нет phone2!!!!! - не могу создать -> не могу найти на странице просмотра

    def get_contact_from_view_page(self, index):
            wd = self.app.wd
            self.open_wiev_page_by_index(index)
            text = wd.find_element_by_id("content").text
            home = re.search("H: (.*)", text).group(1)
            mobile = re.search("M: (.*)", text).group(1)
            work = re.search("W: (.*)", text).group(1)
            # phone2 = re.search("P: (.*)", text).group(1)
            return Contact(phone_home=home, phone_m=mobile, phone_work=work)
            # здесь нет phone2!!!!! - не могу создать -> не могу найти на странице просмотра
