class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group form
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def dell_first(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit del
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def update_first(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open form update
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(group)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        self.up_field_value("group_name", group.name)
        self.up_field_value("group_header", group.header)
        self.up_field_value("group_footer", group.footer)

    def up_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
