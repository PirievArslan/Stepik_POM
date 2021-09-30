from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By




class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "This is not URL for login"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login dorm is not present"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"
        assert True

    def register_new_user(self, email, password):
        self.should_be_register_form()
        self.input_text(*LoginPageLocators.REGISTER_EMAIL_ADDRESS, email)
        self.input_text(*LoginPageLocators.REGISTER_PASSWORD, password)
        self.input_text(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM, password)
        self.click_button(*LoginPageLocators.REGISTER_BUTTON)