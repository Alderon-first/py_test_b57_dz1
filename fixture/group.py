from model.group import Group


class GroupHelper:
    # класс GroupHelper предназначен операций с сущностью "группа": методов создания, удаления и тд
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
        # сбросить кеш - он стал невалидным, потому, что список существующих групп изменился
        self.group_cache = None

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def dell_first(self):
        # удалить первую группу
        self.dell_by_index(0)

    def dell_by_index(self, index):
        # удалить произвольную группу
        wd = self.app.wd
        self.open_groups_page()
        # select group index
        self.select_by_index(index)
        # submit del
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        # сбросить кеш - он стал невалидным, потому, что список существующих групп изменился
        self.group_cache = None

    def update_first(self, group):
        self.update_by_index(0, group)

    def update_by_index(self, index, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_by_index(index)
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(group)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        # сбросить кеш - он стал невалидным, потому, что список существующих групп изменился
        self.group_cache = None

    def fill_group_form(self, group):
        self.up_field_value("group_name", group.name)
        self.up_field_value("group_header", group.header)
        self.up_field_value("group_footer", group.footer)

    def up_field_value(self, field_name, text):
        # метод, описывающий замену значения в форме создания/редактирования группы
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first(self):
        self.select_by_index(0)

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        # посчитать, сколько групп на странице
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        # если group_cache не содержит списка, то создать список
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        # вернуть значение group_cache
        return list(self.group_cache)

    def dell_by_id(self, id):
        # удалить произвольную группу
        wd = self.app.wd
        self.open_groups_page()
        # select group index
        self.select_by_id(id)
        # submit del
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        # сбросить кеш - он стал невалидным, потому, что список существующих групп изменился
        self.group_cache = None

    def select_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="%s"]' % id).click()

    def update_by_id(self, id, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_by_id(id)
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(group)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        # сбросить кеш - он стал невалидным, потому, что список существующих групп изменился
        self.group_cache = None
