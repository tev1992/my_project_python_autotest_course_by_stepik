# главная страница интернет магазина
from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage): # создается класс, который является наследником класса BasePage, чтобы имел доступ ко всем атрибутам и методам класса предка
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # self чтобы иметь доступ к атрибутам и методам класса
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Ссылка на логин не отображается' #*, указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.