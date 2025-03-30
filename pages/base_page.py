from conftest import browser


class BasePage():
    def __init__(self, browser, url): # конструктор - метод который вызывается при создании обьекта
        self.browser = browser # атрибуты класса
        self.url = url # атрибуты класса

    def open(self): # метод открытия страница
        self.browser.get(self.url)