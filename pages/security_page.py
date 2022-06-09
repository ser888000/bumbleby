from time import time
from .base_page import BasePage
from .locators import SecurityPageLocators as locator
import time

class SecurityPage(BasePage):

    def should_be_security_url(self):
        return self.is_text_in_url(locator.TEXT_IN_URL)

    def should_be_security_form(self):
        text = self.get_text(*locator.SECURITY_FORM)
        return locator.SECURITY_FORM_TEXT in text

    def should_be_button_change_tel(self):
        return self.is_element_present(*locator.BUTTON_CHANGE_TEL)

    def should_be_button_change_password(self):
        return self.is_element_present(*locator.BUTTON_CHANGE_PASSWORD)

    def go_to_change_password_tab(self):
        self.btn_click(*locator.BUTTON_CHANGE_PASSWORD)

    def should_be_change_password_form(self):
        text = self.get_text(*locator.CHANGE_PASSWORD_FORM)
        return locator.CHANGE_PASSWORD_FORM_TEXT in text

    def should_be_change_password_form_btn_close(self):
        return self.is_element_present(*locator.CHANGE_PASSWORD_FORM_BTN_CLOSE)

    def should_be_field_old_password(self):
        return self.is_element_present(*locator.OLD_PASSWORD)

    def should_be_field_new_password(self):
        return self.is_element_present(*locator.NEW_PASSWORD)

    def should_be_field_confirm_password(self):
        return self.is_element_present(*locator.CONFIRM_PASSWORD)

    def should_be_button_submit(self):
        return self.is_element_present(*locator.BUTTON_SUBMIT)

    def click_change_password_form_btn_close(self):
        self.btn_click(*locator.CHANGE_PASSWORD_FORM_BTN_CLOSE)

    #------------------------------------------------------------------

    def is_valid_old_password_in_change_password_form(self, value):
        self.set_value(*locator.OLD_PASSWORD, value)
        return self.is_not_element_present(*locator.OLD_PASSWORD_ERROR)

    def is_invalid_old_password_in_change_password_form(self, value):
        self.set_value(*locator.OLD_PASSWORD, value)
        return self.is_element_present(*locator.OLD_PASSWORD_ERROR)

    def is_valid_new_password_in_change_password_form(self, value):
        self.set_value(*locator.NEW_PASSWORD, value)
        return self.is_not_element_present(*locator.NEW_PASSWORD_ERROR)

    def is_invalid_new_password_in_change_password_form(self, value):
        self.set_value(*locator.NEW_PASSWORD, value)
        return self.is_element_present(*locator.NEW_PASSWORD_ERROR)

    def is_valid_confirm_password_in_change_password_form(self, value):
        self.set_value(*locator.CONFIRM_PASSWORD, value)
        return self.is_not_element_present(*locator.CONFIRM_PASSWORD_ERROR)

    def is_invalid_confirm_password_in_change_password_form(self, value):
        self.set_value(*locator.CONFIRM_PASSWORD, value)
        return self.is_element_present(*locator.CONFIRM_PASSWORD_ERROR)

    #------------------------------------------------------------------

    def change_password_valid(self, old_password, new_password):
        # Change password
        self.set_value(*locator.OLD_PASSWORD, old_password)
        self.set_value(*locator.NEW_PASSWORD, new_password)
        self.set_value(*locator.CONFIRM_PASSWORD, new_password)
        self.btn_click(*locator.BUTTON_SUBMIT)
        time.sleep(2)
        text = self.get_text(*locator.PASSWORD_CHANGED_SUCCESSFULLY)
        return locator.PASSWORD_CHANGED_SUCCESSFULLY_TEXT in text
        
    def change_password_invalid(self, old_password, new_password):
        # Change password invalid
        self.set_value(*locator.OLD_PASSWORD, old_password)
        self.set_value(*locator.NEW_PASSWORD, new_password)
        self.set_value(*locator.CONFIRM_PASSWORD, new_password)
        self.btn_click(*locator.BUTTON_SUBMIT)
        return self.is_element_present_wait(*locator.OLD_PASSWORD_ERROR)
        

