from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException 
from selenium.webdriver.common.action_chains import ActionChains
from .locators import BasePageLocators
import math

class BasePage:

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        # окрыть браузер
        self.browser.get(self.url)
            
    def is_element_present(self, how, what):
        # если элемент есть на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=1):
        # если элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        # если элемент исчезает со страницы и через заданное время его уже нет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_text_in_url(self, text):
        # если текс есть текущем url
        return text in self.browser.current_url

    def go_to_login_page(self):
        # Переход на страницу авторизации
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click() 

    def should_be_login_link(self):
        # прверка наличия ссылки на авторизацию
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        # переход в корзину
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click() 

    def is_authorized_user(self):
        # проверка, елси пользователь авторизован, чтобы ошибка не вылетала
        try:
            self.browser.find_element(*BasePageLocators.USER_ICON)
        except NoSuchElementException:
            return False
        return True
 
    def should_be_authorized_user(self):
        # проверка, что пользователь не авторизован
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User is not authorized"
 
    def should_be_not_authorized_user(self):
        # проверка, что пользователь не авторизован
        assert self.is_not_element_present(*BasePageLocators.USER_ICON), "User is authorized"
 
    def logout_user(self):
        # выход из авторизации
        logo_icon = self.browser.find_element(*BasePageLocators.LOGO_ICON)
        ActionChains(self.browser).move_to_element(logo_icon).perform() # указатель мыши на пост, для активации скрытых элементов
        self.browser.find_element(*BasePageLocators.LOGOUT).click() 


