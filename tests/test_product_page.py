import time

from urllib3 import request
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    'links', [
        'offer0', 'offer1', 'offer2' , 'offer3', 'offer4', 'offer5', 'offer6', 'offer8', 'offer9', pytest.param(
            'offer7', marks=pytest.mark.xfail
        )
    ]
)
def test_guest_can_add_product_to_basket(browser, links):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={links}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()
    # language = request.config.getoption("language") #добавлены проверки только для локализации
    page.message_product_added_to_basket() #language=language
    page.message_product_price()


@pytest.mark.xfail(reason='Сообщение отображается, когда добавляем товар в корзину')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.click_button_add_to_basket()
    page.not_message_elements_product_added_to_basket() # проверяем что отсуствует собщение об успехе, при нажатии на добавить


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.not_message_elements_product_added_to_basket()

@pytest.mark.xfail(reason='Элемент не исчезает со страницы за заданное время')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.click_button_add_to_basket()
    page.not_message_element_disappears_product_added_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) #инициализируем LoginPage, передаем экземпляр драйвера и текущий url
    login_page.should_be_login_page()
    time.sleep(4)
