# главная страница интернет магазина

from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): # создается класс, который является наследником класса BasePage, чтобы имел доступ ко всем атрибутам и методам класса предка
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link") # self чтобы иметь доступ к атрибутам и методам класса
        login_link.click()