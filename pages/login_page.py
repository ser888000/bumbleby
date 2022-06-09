from .base_page import BasePage
from .locators import LoginPageLocators as locator
import time

class LoginPage(BasePage):
    

    def should_be_login_url(self):
        return self.is_text_in_url(locator.TEXT_IN_LOGIN_URL)

    def should_be_login_form(self):
        return self.is_element_present(*locator.LOGIN_FORM)

    def should_be_field_email(self):
        return self.is_element_present(*locator.LOGIN_EMAIL)

    def should_be_field_password(self):
        return self.is_element_present(*locator.LOGIN_PASSWORD)

    def should_be_button_submit(self):
        return self.is_element_present(*locator.LOGIN_SUBMIT)

    def should_be_button_registration(self):
        return self.is_element_present(*locator.LOGIN_REGISTRATION)

    def should_be_button_forgot_password(self):
        return self.is_element_present(*locator.FORGOT_PASSWORD)

    #------------------------------------------------------------------

    def is_valid_email_in_login_form(self, value):
        self.set_value(*locator.LOGIN_EMAIL, value)
        return self.is_not_element_present(*locator.LOGIN_EMAIL_EROOR)

    def is_invalid_email_in_login_form(self, value):
        self.set_value(*locator.LOGIN_EMAIL, value)
        return self.is_element_present(*locator.LOGIN_EMAIL_EROOR)

    def is_valid_password_in_login_form(self, value):
        self.set_value(*locator.LOGIN_PASSWORD, value)
        return self.is_not_element_present(*locator.LOGIN_PASSWORD_ERROR)

    def is_invalid_password_in_login_form(self, value):
        self.set_value(*locator.LOGIN_PASSWORD, value)
        return self.is_element_present(*locator.LOGIN_PASSWORD_ERROR)

    #------------------------------------------------------------------

    def login_user(self, email, password):
        self.set_value(*locator.LOGIN_EMAIL, email)
        self.set_value(*locator.LOGIN_PASSWORD, password)
        self.btn_click(*locator.LOGIN_SUBMIT)

    #------------------------------------------------------------------

    def check_ctlr_login_email(self, value1, value2):
        return self.check_ctlr_for_field(*locator.LOGIN_EMAIL, value1, value2)

