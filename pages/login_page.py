from .base_page import BasePage
from .locators import LoginPageLocators 
import time

class LoginPage(BasePage):
    

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert self.is_text_in_url(LoginPageLocators.TEXT_IN_LOGIN_URL), "URL in not login" 

    def should_be_field_form(self):
        # есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "lofin form is not presented" 

    def should_be_field_email(self):
        # есть поле email
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "field email is not presented" 

    def should_be_field_password(self):
        # есть поле password
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "field password is not presented" 

    def should_be_button_submit(self):
        # есть кнопка войти
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "button submit is not presented" 

    def should_be_button_registration(self):
        # есть кнопка регистрации
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTRATION), "button registration is not presented" 

    def should_be_button_forgot_password(self):
        # есть кнопка забыли пароль
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD), "button forgot_password is not presented" 

    def is_valid_email_in_login_form(self, value):
        # проверка на правильный email
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(value)
        assert self.is_not_element_present(*LoginPageLocators.LOGIN_EMAIL_EROOR), f"error input value: {value} to email" 

    def is_not_valid_email_in_login_form(self, value):
        # проверка на недействительный email
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(value)
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_EROOR), f"error input value: {value} to email" 

    def is_valid_password_in_login_form(self, value):
        # проверка на правильный password
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(value)
        assert self.is_not_element_present(*LoginPageLocators.LOGIN_PASSWORD_ERROR), f"error input value: {value} to password" 

    def is_not_valid_password_in_login_form(self, value):
        # проверка на недействительный password
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(value)
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_ERROR), f"error input value: {value} to password" 

    def login_user(self, email, password):
        # Авторизация пользователя
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password) 
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT).click() 

    def check_ctlr_login_email(self, value1, value2):
        # контроль поля ввода email на предмет копирования и вставки значения
        self.check_ctlr_for_field(*LoginPageLocators.LOGIN_EMAIL, value1, value2)

