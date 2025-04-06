from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPagelocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class BasketPageLocators():
    BUTTON_VIEW_BASKET = (By.XPATH, '//span[@class = "btn-group"]//a[contains(@class, "btn-default")]')
    MESSAGE_BASKET_IS_EMPTY = (By.XPATH, '//div[@id = "content_inner"]//p')
    ITEMS_IN_THE_BASKET = (By.XPATH, '//div[@class= "basket-items"]')

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GET_PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    GET_PRODUCT_PRICE = (By.XPATH, '//p[@class = "price_color"][1]')
    MESSAGE_PRODUCT_ADDED = (
    By.XPATH, '''//div[contains(@class, "alertinner")]''')
    MESSAGE_PRODUCT_PRICE = (By.XPATH, '//div[contains(@class, "alertinner")]/p[1]/strong')
