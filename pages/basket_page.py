from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_is_empty(self): #
        actual_result = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY).text
        expected_message = 'Ваша корзина пуста Продолжить покупки'
        assert expected_message == actual_result, \
            f'фактический результат "{actual_result}" не соответствует ожидаемому {expected_message}'  # 'Не отображается текст сообщения "Корзина пустая"'


    def not_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_THE_BASKET), 'В корзине присутствуют товары'

