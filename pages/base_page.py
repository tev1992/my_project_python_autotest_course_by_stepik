# from conftest import browser
from asyncio import timeout

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=5): # конструктор - метод который вызывается при создании обьекта
        self.browser = browser # атрибуты класса
        self.url = url # атрибуты класса
        self.browser.implicitly_wait(timeout)

    def open(self): # метод открытия страница
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

