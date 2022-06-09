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

    def should_be_button_change_phone(self):
        return self.is_element_present(*locator.BUTTON_CHANGE_PHONE)

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

    def should_be_button_submit_password(self):
        return self.is_element_present(*locator.BUTTON_SUBMIT_PASSWORD)

    def click_change_password_form_btn_close(self):
        self.btn_click(*locator.CHANGE_PASSWORD_FORM_BTN_CLOSE)

    #-----------is_valid-------------------------------------------------------

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

    #----------------change_password--------------------------------------------------

    def change_password_valid(self, old_password, new_password):
        # Change password
        self.set_value(*locator.OLD_PASSWORD, old_password)
        self.set_value(*locator.NEW_PASSWORD, new_password)
        self.set_value(*locator.CONFIRM_PASSWORD, new_password)
        self.btn_click(*locator.BUTTON_SUBMIT_PASSWORD)
        time.sleep(2)
        text = self.get_text(*locator.PASSWORD_CHANGED_SUCCESSFULLY)
        return locator.PASSWORD_CHANGED_SUCCESSFULLY_TEXT in text
        
    def change_password_invalid(self, old_password, new_password):
        # Change password invalid
        self.set_value(*locator.OLD_PASSWORD, old_password)
        self.set_value(*locator.NEW_PASSWORD, new_password)
        self.set_value(*locator.CONFIRM_PASSWORD, new_password)
        self.btn_click(*locator.BUTTON_SUBMIT_PASSWORD)
        return self.is_element_present_wait(*locator.OLD_PASSWORD_ERROR)
        
    #-----------should_be-------------------------------------------------------

    def go_to_change_phone_tab(self):
        self.btn_click(*locator.BUTTON_CHANGE_PHONE)

    def should_be_change_phone_form(self):
        text = self.get_text(*locator.CHANGE_PHONE_FORM)
        return locator.CHANGE_PHONE_FORM_TEXT in text

    def should_be_change_phone_form_btn_close(self):
        return self.is_element_present(*locator.CHANGE_PHONE_FORM_BTN_CLOSE)

    def should_be_field_phone(self):
        return self.is_element_present(*locator.PHONE)

    def should_be_button_submit_phone(self):
        return self.is_element_present(*locator.BUTTON_SUBMIT_PHONE)

    def click_change_phone_form_btn_close(self):
        self.btn_click(*locator.CHANGE_PHONE_FORM_BTN_CLOSE)

    #-----------is_valid_phone-------------------------------------------------------
    
    def is_valid_phone_in_change_phone_form(self, value):
        self.set_value(*locator.PHONE, value)
        get_value = self.get_value(*locator.PHONE)
        # если нет сообщения об ошибке и 10 последних цифр в поле совпадаютс тем, что в него вводили
        return (self.is_not_element_present(*locator.PHONE_ERROR) and
            ''.join(i for i in get_value if i.isdigit())[-10:] == 
            ''.join(i for i in value if i.isdigit())[-10:]
            )

    def is_invalid_phone_in_change_phone_form(self, value):
        self.set_value(*locator.PHONE, value)
        get_value = self.get_value(*locator.PHONE)
        # если есть сообщение об ошибке или кнопка Подтвердить заблокирована 
        # или 10 последних цифр в поле не совпадают с тем, что в него вводили
        try:
            if (''.join(i for i in get_value if i.isdigit())[-10:] != 
            ''.join(i for i in value if i.isdigit())[-10:]):
                return True
        except:
            return True
        return (self.is_element_present(*locator.PHONE_ERROR) or
            self.is_element_present(*locator.BUTTON_SUBMIT_PHONE_DISABLED))

    #-------------change_phone-----------------------------------------------------

    def change_phone_valid(self, value):
        self.set_value(*locator.PHONE, value)
        self.btn_click(*locator.BUTTON_SUBMIT_PHONE)
        time.sleep(2)
        text = self.get_text(*locator.PHONE_CHANGED_SUCCESSFULLY)
        get_value = self.get_value(*locator.PHONE)
        # если есть текст 'Номер телефона успешно изменен!' и цифры совпадают
        return (locator.PHONE_CHANGED_SUCCESSFULLY_TEXT in text and
            ''.join(i for i in get_value if i.isdigit())[-10:] == 
            ''.join(i for i in value if i.isdigit())[-10:])
        
    def change_phone_invalid(self, value):
        self.set_value(*locator.PHONE, value)
        self.btn_click(*locator.BUTTON_SUBMIT_PHONE)
        return self.is_element_present_wait(*locator.BUTTON_SUBMIT_PHONE_DISABLED)
        
