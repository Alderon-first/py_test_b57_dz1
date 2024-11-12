from model.contact import Contact


class ContactHelper:
    # класс ContactHelper предназначен операций с сущностью "контакт": методов создания, удаления и тд
    def __init__(self, app):
        self.app = app

    def open_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        # init group creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit group form
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()

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
        # выбрать первую
        wd.find_element_by_name("selected[]").click()
        # удалить первую группу
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()

    def update_first(self, contact):
        wd = self.app.wd
        # выбрать первую
        wd.find_element_by_name("selected[]").click()
        # изменить выбранную
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[21]").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.open_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_to_home_page()
        contscts = []
        for element in wd.find_elements_by_name("entry"):
            lastname = element.find_elements_by_css_selector("td")[1].text
            firstname = element.find_elements_by_css_selector("td")[2].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contscts.append(Contact(first_name=firstname, last_name=lastname, id=id))
        return list(contscts)


