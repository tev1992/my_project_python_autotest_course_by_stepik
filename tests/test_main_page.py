from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import config
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, config.BASE_URL) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url) #инициализируем LoginPage, передаем экземпляр драйвера и текущий url
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, config.BASE_URL)
        page.open()
        page.should_be_login_link()

@pytest.mark.basket_quest
class TestBasketFromMainPage():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = BasketPage(browser, config.BASE_URL)
        page.open() #открываем главную страницу
        page.should_be_basket_button() # проверяем наличие кнопки "Перейти в корзину"
        page.go_to_basket_page() # переходим в корзину
        page.should_be_basket_is_empty() # проверяем сообщение, что корзина пуста
        page.not_items_in_the_basket() # проверка отсутствия товара в корзине


