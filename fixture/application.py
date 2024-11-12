from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver - для хрома
from selenium.webdriver.firefox.options import Options
from fixture.sesion import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    # класс Application предназначен для создания сессии и методов взаимодействия с ней
    def __init__(self):
        # self.wd = WebDriver() - для хрома
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\Windows\System32\geckodriver.exe', options=options)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        # сессия валидна: проверяем, что браузер еще существует, проверяя наличие урла
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()



