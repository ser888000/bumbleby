from .base_page import BasePage
from .locators import LoginPageLocators as locator
import time

class LoginPage(BasePage):
    

    def should_be_login_url(self):
        # проверка на корректный url адрес
        return self.is_text_in_url(locator.TEXT_IN_LOGIN_URL)

    def should_be_field_form(self):
        # есть форма логина
        return self.is_element_present(*locator.LOGIN_FORM)

    def should_be_field_email(self):
        # есть поле email
        return self.is_element_present(*locator.LOGIN_EMAIL)

    def should_be_field_password(self):
        # есть поле password
        return self.is_element_present(*locator.LOGIN_PASSWORD)

    def should_be_button_submit(self):
        # есть кнопка войти
        return self.is_element_present(*locator.LOGIN_SUBMIT)

    def should_be_button_registration(self):
        # есть кнопка регистрации
        return self.is_element_present(*locator.LOGIN_REGISTRATION)

    def should_be_button_forgot_password(self):
        # есть кнопка забыли пароль
        return self.is_element_present(*locator.FORGOT_PASSWORD)

    def is_valid_email_in_login_form(self, value):
        # проверка на правильный email
        self.browser.find_element(*locator.LOGIN_EMAIL).send_keys(value)
        return self.is_not_element_present(*locator.LOGIN_EMAIL_EROOR)

    def is_invalid_email_in_login_form(self, value):
        # проверка на недействительный email
        self.browser.find_element(*locator.LOGIN_EMAIL).send_keys(value)
        return self.is_element_present(*locator.LOGIN_EMAIL_EROOR)

    def is_valid_password_in_login_form(self, value):
        # проверка на правильный password
        self.browser.find_element(*locator.LOGIN_PASSWORD).send_keys(value)
        return self.is_not_element_present(*locator.LOGIN_PASSWORD_ERROR)

    def is_invalid_password_in_login_form(self, value):
        # проверка на недействительный password
        self.browser.find_element(*locator.LOGIN_PASSWORD).send_keys(value)
        return self.is_element_present(*locator.LOGIN_PASSWORD_ERROR)

    def login_user(self, email, password):
        # Авторизация пользователя
        self.browser.find_element(*locator.LOGIN_EMAIL).send_keys(email)
        self.browser.find_element(*locator.LOGIN_PASSWORD).send_keys(password) 
        self.browser.find_element(*locator.LOGIN_SUBMIT).click() 

    def check_ctlr_login_email(self, value1, value2):
        # контроль поля ввода email на предмет копирования и вставки значения
        return self.check_ctlr_for_field(*locator.LOGIN_EMAIL, value1, value2)

