from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".registration__profile .avatar_icon")
    LOGO_ICON = (By.CSS_SELECTOR, ".logo_icon")
    LOGOUT = (By.CSS_SELECTOR, ".logout")
    

class LoginPageLocators():
    TEXT_IN_LOGIN_URL = "login"
    
    LOGIN_FORM = (By.CSS_SELECTOR, ".login-form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, ".field [type='text']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, ".field [type='password']")
    LOGIN_EMAIL_EROOR = (By.CSS_SELECTOR, ".field [type='text'][class='has-error']")
    LOGIN_PASSWORD_ERROR = (By.CSS_SELECTOR, ".field [type='password'][class='has-error']")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[type='submit']")
    LOGIN_REGISTRATION = (By.CSS_SELECTOR, "[type='registration']")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "[type='submit']")
    


class ProductPageLocators():
    TEXT_IN_URL = "promo"
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE_IN_MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

class BasketPageLocators():
    BASKET_TOTAL = (By.CSS_SELECTOR, ".total")
    BASKET_EMPTY = (By.CSS_SELECTOR, ".content #content_inner > p")
