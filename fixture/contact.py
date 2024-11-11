class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
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
