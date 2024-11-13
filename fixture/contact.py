from model.contact import Contact


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
        self.up_field_value("email", contact.email)

    def up_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def dell_first(self):
        wd = self.app.wd
        self.open_home_page()
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
        self.open_home_page()
        wd = self.app.wd
        self.select_by_index(0, contact)

    def update_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        # изменить выбранную
        self.open_by_index(index)
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_by_index(self, index):
        wd = self.app.wd
        print(index)
        wd.find_elements_by_name("entry")[index].find_elements_by_tag_name("td")[7].find_element_by_tag_name("a").click()

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
        wd = self.app.wd
        self.open_home_page()
        self.contact_cache = []
        for element in wd.find_elements_by_name("entry"):
            lastname = element.find_elements_by_css_selector("td")[1].text
            firstname = element.find_elements_by_css_selector("td")[2].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            self.contact_cache.append(Contact(first_name=firstname, last_name=lastname, id=id))
        return list(self.contact_cache)


