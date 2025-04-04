from urllib3 import request
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser, request):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()
    # language = request.config.getoption("language") #добавлены проверки только для локализации
    page.message_product_added_to_basket() #language=language
    page.message_product_price()




