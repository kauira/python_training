from _pytest.main import Session
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        firefox_options = Options()
        firefox_binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        firefox_options.binary_location = firefox_binary_path
        self.wd = webdriver.Firefox(options=firefox_options)
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")

    def destroy(self):
        self.wd.quit()