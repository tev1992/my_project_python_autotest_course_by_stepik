from pages.base_page import BasePage
from pages.locators import LoginPagelocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in  self.url, f"'login' не содержится в ссылке"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPagelocators.LOGIN_FORM), 'login_Form не отбражается'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPagelocators.REGISTER_FORM), 'register_Form не отбражается'