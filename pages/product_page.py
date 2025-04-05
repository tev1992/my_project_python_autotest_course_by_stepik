import time
from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    PRODUCT_ADDED_MESSAGES = {
        'en': "has been added to your basket.",
        'ru': "был добавлен в вашу корзину.",
        # Добавьте другие языки по необходимости
    }

    PRODUCT_PRICE_MESSAGE = {
        'ru': "57,96 £"
    }

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BOTTON_ADD_TO_BASKET), 'Кнопка "Добавить в корзину" не отображается на странице'

    def click_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BOTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def get_price_product_text(self):
        price_element_text = self.browser.find_element(*ProductPageLocators.GET_PRODUCT_PRICE).text
        print(price_element_text)
        return price_element_text

    def get_product_name_text(self):
        product_name = self.browser.find_element(*ProductPageLocators.GET_PRODUCT_NAME).text
        print(product_name)
        return product_name

    def message_product_added_to_basket(self): #language
        expected_messege = f"{self.get_product_name_text()} {self.PRODUCT_ADDED_MESSAGES['ru']}"
        actual_messege = self.browser.find_element(*ProductPageLocators.MESSEGE_PRODUCT_ADDED).text #(self.PRODUCT_ADDED_MESSAGES.get(language, self.PRODUCT_ADDED_MESSAGES))
        assert expected_messege == actual_messege, F'"{actual_messege}" не соответсвует ожидаемому результату: "{expected_messege}"'

    def message_product_price(self):
        expectes_messege = self.get_price_product_text()
        actual_message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text
        assert expectes_messege == actual_message, F'"{actual_message}" не соответсвует ожидаемому результату: "{expectes_messege}"'











