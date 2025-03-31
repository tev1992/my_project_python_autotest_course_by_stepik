import time
from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    PRODUCT_ADDED_MESSAGES = {
        'en': "The shellcoder's handbook has been added to your basket.",
        'ru': "The shellcoder's handbook был добавлен в вашу корзину.",
        # Добавьте другие языки по необходимости
    }

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BOTTON_ADD_TO_BASKET), 'Кнопка "Добавить в корзину" не отображается на странице'

    def click_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BOTTON_ADD_TO_BASKET)
        button_add_to_basket.click()


    def product_added_to_basket(self, language):
        expected_messege = self.PRODUCT_ADDED_MESSAGES.get(language, self.PRODUCT_ADDED_MESSAGES)
        actual_messege = self.browser.find_element(*ProductPageLocators.MESSEGE_PRODUCT_ADDED).text
        assert expected_messege == actual_messege, F'"{actual_messege}" не соответсвует ожидаемому результату: "{expected_messege}"'











