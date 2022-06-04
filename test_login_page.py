from multiprocessing.sharedctypes import Value
from .pages.login_page import LoginPage
import pytest
import time
from .lib.combinatorics import all_pairs2 as ap

#===========================================================
link = 'https://app.neapro.site'
link_login = link + '/login'
email = 'cto8@ya.ru'
password = '12345678'
# список недействительных данных для попарного тестирования авторизации (почта, пароль)
email_password_negative = list(ap.all_pairs2([
        ['fake@fakemail.ru', ''],
        ['11111111', '']
        ]))
# список действительных данных для проверки поля почта
email_positive = ['', 'fake@fakemail.ru']
# список недействительных данных для проверки поля почта
email_negative = [' ', 'fake', 'fake.ru', 'fake@', '0000']
# список действительных данных для проверки поля пароль
password_positive = ['', 'qwertyui', 'qawsedrfg', '123456789', '!@#$%^&*', '(@#$%^&*)']
# список недействительных данных для проверки поля пароль
password_negative = [' ']
#===========================================================

pytest.mark.new
class TestLoginPageIsElements():
    def test_should_be_login_url(self, browser):
        # проверка url
        page = LoginPage(browser, link_login)      
        page.open()
        page.should_be_login_url() 

    def test_should_be_login_form(self, browser):
        # проверка формы логина
        page = LoginPage(browser, link_login)      
        page.open()
        page.should_be_field_form() 

    @pytest.mark.parametrize('arr', email_positive) 
    def test_check_field_email_positive(self, browser, arr):
        # проверка email на допустимые значения
        page = LoginPage(browser, link_login)      
        page.open()
        page.should_be_field_email() 
        page.is_valid_email_in_login_form(arr)

    @pytest.mark.negative
    @pytest.mark.parametrize('arr', email_negative) 
    def test_check_field_email_negative(self, browser, arr):
        # проверка email на допустимые значения
        page = LoginPage(browser, link_login)      
        page.open()
        page.should_be_field_email() 
        page.is_not_valid_email_in_login_form(arr)

    @pytest.mark.parametrize('arr', password_positive) 
    def test_check_field_password_positive(self, browser, arr):
        # проверка password на допустимые значения
        page = LoginPage(browser, link_login)      
        page.open()
        page.should_be_field_password() 
        page.is_valid_password_in_login_form(arr)

    @pytest.mark.negative
    @pytest.mark.parametrize('arr', password_negative) 
    def test_check_field_password_negative(self, browser, arr):
        # проверка password на допустимые значения
        page = LoginPage(browser, link_login)      
        page.open()
        page.should_be_field_password() 
        page.is_not_valid_password_in_login_form(arr)

    def test_should_be_button_submit(self, browser):
        # проверка кнопки войти
        page = LoginPage(browser, link + '/login')      
        page.open()
        page.should_be_button_submit() 

    def test_should_be_button_registration(self, browser):
        # проверка кнопки регистрация
        page = LoginPage(browser, link + '/login')      
        page.open()
        page.should_be_button_registration() 

    def test_should_be_button_forgot_password(self, browser):
        # проверка кнопки забыли пароль
        page = LoginPage(browser, link + '/login')      
        page.open()
        page.should_be_button_forgot_password() 

#@pytest.mark.new
class TestLoginPageLogin():
    @pytest.mark.new
    def test_login_user(self, browser):
        # авторизация пользователя
        page = LoginPage(browser, link_login)      
        page.open()
        page.login_user(email, password) # авторизация пользователя 
        page.should_be_authorized_user() # проверка что пользователь авторизован

    @pytest.mark.negative
    @pytest.mark.parametrize('arr', email_password_negative)    
    def test_login_user_negative(self, browser, arr):
        # аторизация с негативными данными почты и пароля
        page = LoginPage(browser, link_login)      
        page.open()
        page.login_user(*arr) # авторизация пользователя 
        page.should_be_not_authorized_user() # проверка отсутствия авторизации




