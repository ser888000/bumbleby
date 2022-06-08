from .pages.security_page import SecurityPage
import pytest
import time
from .data import *


#===========================================================
url = '/cabinet/security'

@pytest.mark.new
def test_empty(login_fixture): # не знаю пока как написать логин, фикстура находится в conftest.py
    pass

@pytest.mark.new
class TestSecurityPageCheckElements():
    
    def test_should_be_security_url(self, browser):
        # проверка url
        page = SecurityPage(browser, url)      
        page.open()
        time.sleep(1)
        # ==== steps ====
        assert page.should_be_security_url(), "URL in not security" 

    def test_should_be_security_form(self, browser):
        # проверка формы логина
        page = SecurityPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_security_form(), "security form is not presented"  

    def test_should_be_button_change_tel(self, browser):
        # проверка button_change_tel
        page = SecurityPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_button_change_tel(), "button_change_tel is not presented"  

    def test_should_be_button_change_password(self, browser):
        # проверка button_change_password
        page = SecurityPage(browser, url)      
        page.open()
        # ==== steps ====
        assert page.should_be_button_change_password(), 'button_change_passwordl is not presented' 

    def test_should_be_change_password_form(self, browser):
        # проверка change_password_form
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        assert page.should_be_change_password_form(), "change_password_form is not presented" 

    def test_should_be_change_password_form_btn_close(self, browser):
        # проверка password_form_btn_close
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        assert page.should_be_change_password_form_btn_close(), "password_form_btn_close is not presented" 

    def test_should_be_field_old_password(self, browser):
        # проверка field_old_password
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        assert page.should_be_field_old_password(), "field_old_password is not presented" 

    def test_should_be_field_new_password(self, browser):
        # проверка field_new_password
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        assert page.should_be_field_new_password(), "field_new_password is not presented" 

    def test_should_be_field_confirm_password(self, browser):
        # проверка field_confirm_password
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        assert page.should_be_field_confirm_password(), "field_confirm_password is not presented" 

    def test_should_be_button_submit(self, browser):
        # проверка button_submit
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        assert page.should_be_button_submit(), "button_submit is not presented" 

    def test_click_change_password_form_btn_close(self, browser):
        # проверка password_form_btn_close
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        page.click_change_password_form_btn_close()
        assert page.should_be_security_form(), "password_form_btn_close is not click" 

    @pytest.mark.parametrize('data', password_valid) 
    def test_check_is_valid_old_password_in_change_password_form(self, browser, data):
        # проверка password на допустимые значения
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        assert page.is_valid_old_password_in_change_password_form(data), f"ERROR input value: {data} to password" 

    @pytest.mark.negative
    @pytest.mark.parametrize('data', password_invalid) 
    def test_check_is_invalid_old_password_in_change_password_form(self, browser, data):
        # проверка password на допустимые значения
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        assert page.is_invalid_old_password_in_change_password_form(data), f"NEGATIVE error input value: {data} to password" 

    @pytest.mark.parametrize('data', password_valid) 
    def test_check_is_valid_new_password_in_change_password_form(self, browser, data):
        # проверка password на допустимые значения
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        assert page.is_valid_new_password_in_change_password_form(data), f"ERROR input value: {data} to password" 

    @pytest.mark.negative
    @pytest.mark.parametrize('data', password_invalid) 
    def test_check_is_invalid_new_password_in_change_password_form(self, browser, data):
        # проверка password на допустимые значения
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
        assert page.is_invalid_new_password_in_change_password_form(data), f"NEGATIVE error input value: {data} to password" 

    @pytest.mark.parametrize('data', password_valid) 
    def test_check_is_valid_confirm_password_in_change_password_form(self, browser, data):
        # проверка password на допустимые значения
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        page.is_invalid_new_password_in_change_password_form(data)
        # ==== steps ====
        assert page.is_valid_confirm_password_in_change_password_form(data), f"ERROR input value: {data} to password" 

    @pytest.mark.negative
    @pytest.mark.parametrize('data', password_valid) 
    def test_check_is_invalid_confirm_password_in_change_password_form(self, browser, data):
        # проверка password на допустимые значения
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        page.is_invalid_new_password_in_change_password_form(data)
        # ==== steps ====
        assert page.is_invalid_confirm_password_in_change_password_form(data + '1'), f"NEGATIVE error input value: {data} to password" 

    def test_change_password_valid(self, browser):
        # изменение пароля
        # ---- precondition ----
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
         # изменение пароля 
        assert page.change_password_valid(password, new_password), "FAIL: User password not successfully changed" 
        # ---- postcondition ----
        page.open()
        page.go_to_change_password_tab()
        page.change_password_valid(new_password, password)
        

    def test_change_password_invalid(self, browser):
        # изменение пароля
        # ---- precondition ----
        page = SecurityPage(browser, url)      
        page.open()
        page.go_to_change_password_tab()
        # ==== steps ====
         # изменение пароля 
        assert page.change_password_invalid(invalid_password, password), "NEGATIVE FAIL: User password successfully changed" 
        # ---- postcondition ----

        

