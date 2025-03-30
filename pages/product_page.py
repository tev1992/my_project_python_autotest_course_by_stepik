import time

from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BOTTON_ADD_TO_BASKET), 'Кнопка "Добавить в корзину" не отображается на странице'

    def click_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BOTTON_ADD_TO_BASKET)
        button_add_to_basket.click()









