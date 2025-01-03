class SessionHelper:
    # класс SessionHelper предназначен операций с сессией после ее создания через Application: логин/логаут,
    # проверка статуса
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        return self.get_logget_user() == username

    def get_logget_user(self):
        # получает из браузера имя пользователя в формате (username). отрезаем скобки
        wd = self.app.wd
        return  wd.find_element_by_xpath("//*[@id='top']/form/b").text[1:-1]

    def is_logged_in(self):
        # ссылок с текстом Logout больше 0
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
