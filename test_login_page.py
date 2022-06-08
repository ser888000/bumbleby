from .pages.login_page import LoginPage
import pytest
import time
from .data import *

#===========================================================
url = '/login'

#@pytest.mark.new
class TestLoginPageCheckElements():
    def test_should_be_login_url(self, browser):
        # проверка url
        page = LoginPage(browser, url)      
        page.open()
        time.sleep(1)
        # ==== steps ====
        assert page.should_be_login_url(), "URL in not login" 

    def test_should_be_login_form(self, browser):
        # проверка формы логина
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_field_form(), "login form is not presented"  

    def test_should_be_login_email(self, browser):
        # проверка поля email 
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_field_email(), "field email is not presented"  

    @pytest.mark.parametrize('data', email_valid) 
    def test_check_field_email_positive(self, browser, data):
        # проверка email на допустимые значения
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.is_valid_email_in_login_form(data), f"ERROR input value: {data} to email" 

    @pytest.mark.negative
    @pytest.mark.parametrize('data', email_invalid) 
    def test_check_field_email_negative(self, browser, data):
        # проверка email на недопустимые значения
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.is_invalid_email_in_login_form(data), f"NEGATIVE error input value: {data} to email" 

    def test_ctrl_email(self, browser):
        # контроль поля ввода email на предмет копирования и вставки значения
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.check_ctlr_login_email('wwwwww', 'eeeeee'), "ERROR Ctrl+c and Ctrl+v"

    def test_should_be_login_password(self, browser):
        # проверка password что есть
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_field_password(), "field password is not presented" 

    @pytest.mark.new
    @pytest.mark.parametrize('data', password_valid) 
    def test_check_field_password_positive(self, browser, data):
        # проверка password на допустимые значения
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.is_valid_password_in_login_form(data), f"ERROR input value: {data} to password" 

    @pytest.mark.new
    @pytest.mark.negative
    @pytest.mark.parametrize('data', password_invalid) 
    def test_check_field_password_negative(self, browser, data):
        # проверка password на допустимые значения
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.is_invalid_password_in_login_form(data), f"NEGATIVE error input value: {data} to password" 

    def test_should_be_button_submit(self, browser):
        # проверка кнопки войти
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_button_submit(), "button submit is not presented"  

    def test_should_be_button_registration(self, browser):
        # проверка кнопки регистрация
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_button_registration() , "button registration is not presented" 

    def test_should_be_button_forgot_password(self, browser):
        # проверка кнопки забыли пароль
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_button_forgot_password(), "button forgot_password is not presented"  



#@pytest.mark.new
class TestLoginPageLogin():
#    @pytest.mark.new
    def test_login_user(self, browser):
        # авторизация пользователя
        # ---- precondition ----
        page = LoginPage(browser, url)      
        page.open()
        page.logout_user() # выход из авторизации, если есть авторизация
        # ==== steps ====
        page.login_user(*login_password_valid) # авторизация пользователя 
        # ---- check ----
        assert page.should_be_authorized_user(), "FAIL: User is not authorized" 
        # ---- postcondition ----
        page.logout_user() # выход из авторизации

    @pytest.mark.negative
    @pytest.mark.parametrize('data', login_password_pairs_invalid)    
    def test_login_user_negative(self, browser, data):
        # аторизация с негативными данными почты и пароля
        # ---- precondition ----
        page = LoginPage(browser, url)      
        page.open()
        page.logout_user() # выход из авторизации, если есть авторизация
        # ==== steps ====
        page.login_user(*data) # авторизация пользователя 
        assert page.should_be_not_authorized_user(), "NEGATIVE FAIL: User is authorized" 
        # ---- postcondition ----
        page.logout_user() # выход из авторизации





