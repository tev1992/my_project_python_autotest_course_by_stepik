import time

from urllib3 import request
import pytest

import config
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage

class TestPromoLinkProductPage():
    @pytest.mark.parametrize(
        'links', [
            '?promo=offer0', '?promo=offer1', '?promo=offer2' , '?promo=offer3', '?promo=offer4', \
                '?promo=offer5', '?promo=offer6', '?promo=offer8', '?promo=offer9', pytest.param(
                '?promo=offer7', marks=pytest.mark.xfail
            )
        ]
    )
    def test_guest_can_add_product_to_basket(self, browser, links):
        # link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{links}'
        page = ProductPage(browser, f'{config.PRODUCT_URL_ONE}{links}')
        page.open()
        page.should_be_add_to_basket()
        page.click_button_add_to_basket()
        page.solve_quiz_and_get_code()
        # language = request.config.getoption("language") #добавлены проверки только для локализации
        page.message_product_added_to_basket() #language=language
        page.message_product_price()


@pytest.mark.xfail(reason='Сообщение отображается, когда добавляем товар в корзину')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, config.PRODUCT_URL_ONE)
    page.open()
    page.should_be_add_to_basket()
    page.click_button_add_to_basket()
    page.not_message_elements_product_added_to_basket() # проверяем что отсуствует собщение об успехе, при нажатии на добавить


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, TestPromoLinkProductPage)
    page.open()
    page.not_message_elements_product_added_to_basket()

@pytest.mark.xfail(reason='Элемент не исчезает со страницы за заданное время')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, config.PRODUCT_URL_ONE)
    page.open() # открываем страницу
    page.should_be_add_to_basket() # проверяем, что кнопка "Добавить в корзину" отображается на странице
    page.click_button_add_to_basket() # добавляем товар в корзину
    page.not_message_element_disappears_product_added_to_basket() #  проверяем, что сообщение о добавление в корзину не исчезает

@pytest.mark.login
class TestLoginFromProductPage():
    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self):
    #     self.product = ProductFactory(title = "Новый продукт созданные по API")
    #     # создаем по апи
    #     self.link = self.product.link
    #     yield
    #     # после этого ключевого слова начинается teardown
    #     # выполнится после каждого теста в классе
    #     # удаляем те данные, которые мы создали
    #     self.product.delete()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, config.PRODUCT_URL_TWO)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = ProductPage(browser, config.BASE_URL) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url) #инициализируем LoginPage, передаем экземпляр драйвера и текущий url
        login_page.should_be_login_page()

class TestBasketFromProductPage():
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = BasketPage(self, browser, config.PRODUCT_URL_TWO)
        page.open() #открываем страницу
        page.should_be_basket_button() # проверяем наличие кнопки "Перейти в корзину"
        page.go_to_basket_page() # переходим в корзину
        page.should_be_basket_is_empty() # проверяем сообщение, что корзина пуста
        page.not_items_in_the_basket() # проверка отсутствия товара в корзине

