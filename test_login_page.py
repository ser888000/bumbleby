from .pages.login_page import LoginPage
import pytest
import time
from .data import *

#===========================================================
url = '/login'

#@pytest.mark.new
class TestLoginPageCheckElements():
    def test_should_be_login_url(self, browser):
        page = LoginPage(browser, url)      
        page.open()
        time.sleep(1)
        # ==== steps ====
        assert page.should_be_login_url(), "URL in not login" 

    def test_should_be_login_form(self, browser):
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_login_form(), "login form is not presented"  

    def test_should_be_login_email(self, browser):
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_field_email(), "field email is not presented"  

    @pytest.mark.parametrize('data', emails_valid) 
    def test_check_field_email_positive(self, browser, data):
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.is_valid_email_in_login_form(data), f"ERROR input value: {data} to email" 

    @pytest.mark.negative
    @pytest.mark.parametrize('data', emails_invalid) 
    def test_check_field_email_invalid(self, browser, data):
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.is_invalid_email_in_login_form(data), f"NEGATIVE error input value: {data} to email" 

    def test_ctrl_email(self, browser):
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.check_ctlr_login_email('wwwwww', 'eeeeee'), "ERROR Ctrl+c and Ctrl+v"

    def test_should_be_login_password(self, browser):
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_field_password(), "field password is not presented" 

    @pytest.mark.parametrize('data', passwords_valid) 
    def test_check_field_password_positive(self, browser, data):
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.is_valid_password_in_login_form(data), f"ERROR input value: {data} to password" 

    @pytest.mark.negative
    @pytest.mark.parametrize('data', passwords_invalid) 
    def test_check_field_password_invalid(self, browser, data):
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.is_invalid_password_in_login_form(data), f"NEGATIVE error input value: {data} to password" 

    def test_should_be_button_submit(self, browser):
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_button_submit(), "button submit is not presented"  

    def test_should_be_button_registration(self, browser):
        page = LoginPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_button_registration() , "button registration is not presented" 

    def test_should_be_button_forgot_password(self, browser):
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
    def test_login_user_invalid(self, browser, data):
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





