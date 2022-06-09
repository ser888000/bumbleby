from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from .locators import BasePageLocators as locator
import time

class BasePage:
    
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
#        self.base_url = 'https://app.neapro.site'
        self.base_url = 'https://bumbleby.ru'
        self.url = self.base_url + url
        self.browser.implicitly_wait(timeout)

    def open(self):
        # окрыть браузер
        self.browser.get(self.url)

    def refresh_page(self):
        # окрыть браузер
        self.browser.refresh()

    def get_url(self):
        # текущий uel
        return self.browser.current_url

    def get_title(self):
        # заголовок браузера
        return self.browser.title      

    def hover(self, how, what):
        # указатель мыши на элемент, для активации скрытых элементов
        element = self.browser.find_element(how, what)
        ActionChains(self.browser).move_to_element(element).perform()          
            
    def is_element_present(self, how, what):
        # если элемент есть на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException as err:
            return False
        return True

    def is_element_present_wait(self, how, what, timeout=4):
        # если элемент появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
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
        return text in self.get_url()

    def go_to_login_page(self):
        # Переход на страницу авторизации
        login_link = self.browser.find_element(*locator.LOGIN_LINK)
        login_link.click() 

    def should_be_login_link(self):
        # прверка наличия ссылки на авторизацию
        return self.is_element_present(*locator.LOGIN_LINK)

    def go_to_basket_page(self):
        # переход в корзину
        basket_link = self.browser.find_element(*locator.BASKET_LINK)
        basket_link.click() 

    def should_be_authorized_user(self):
        # проверка, что пользователь авторизован
        return self.is_element_present(*locator.USER_ICON)
        
    def should_be_not_authorized_user(self):
        # проверка, что пользователь не авторизован
        return self.is_not_element_present(*locator.USER_ICON, 1)
 
    def logout_user(self):
        # выход из авторизации
        if self.is_not_element_present(*locator.USER_ICON, 1): return
        self.hover(*locator.LOGO_ICON) # указатель мыши на пост, для активации скрытых элементов
        self.browser.find_element(*locator.LOGOUT).click() 

    def check_ctlr_for_field(self, how, what, value1, value2):
        # контроль поля ввода на предмет копирования и вставки значения
        elem = self.browser.find_element(how, what)
        elem.clear()
        elem.send_keys(value1)
        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.CONTROL + "c")
        elem.send_keys(value2)
        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.CONTROL + "v")
        value_field = elem.get_property("value")
        return value_field == value1

    def set_value(self, how, what, value, timeout=5):
        elem = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        elem.clear()
        elem.send_keys(value)

    def get_text(self, how, what, timeout=5):
        elem = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        return elem.text

    def btn_click(self, how, what, timeout=5):
        elem = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        elem.click()



