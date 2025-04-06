from operator import truediv
from .locators import MainPageLocators, BasePageLocators, BasketPageLocators
from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=5): # конструктор - метод который вызывается при создании обьекта
        self.browser = browser # атрибуты класса
        self.url = url # атрибуты класса
        self.browser.implicitly_wait(timeout)

    def open(self): # метод открытия страница
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)  # self чтобы иметь доступ к атрибутам и методам класса
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            'Ссылка на логин не отображается'  # *, указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BUTTON_VIEW_BASKET)
        basket_link.click()

    def should_be_basket_button(self):
        assert self.is_element_present(*BasketPageLocators.BUTTON_VIEW_BASKET), \
            'Кнопка "Перейти в козину" не отображается'

    def is_element_present(self, how, what): #Элемент есть на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4): # метод, который проверяет, \
        # что элемент не появляется на странице в течении задан. времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4): #служит для проверки, что элемент исчезает со страницы в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


