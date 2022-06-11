from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".registration__profile .avatar_icon")
    LOGO_ICON = (By.CSS_SELECTOR, ".logo_icon")
    LOGOUT = (By.CSS_SELECTOR, ".logout")
    

class LoginPageLocators():
    TEXT_IN_LOGIN_URL = "login"
    
    LOGIN_FORM = (By.CSS_SELECTOR, ".body .login-form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, ".field [type='text']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, ".field [type='password']")
    LOGIN_EMAIL_EROOR = (By.CSS_SELECTOR, ".field [type='text'][class='has-error']")
    LOGIN_PASSWORD_ERROR = (By.CSS_SELECTOR, ".field [type='password'][class='has-error']")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[type='submit']")
    LOGIN_REGISTRATION = (By.CSS_SELECTOR, "[type='registration']")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "[type='submit']")
    


class SecurityPageLocators():
    TEXT_IN_URL = "security"
    SECURITY_FORM = (By.CSS_SELECTOR, ".form > .form-title")
    SECURITY_FORM_TEXT = 'Безопасность и вход'
    BUTTON_CHANGE_PHONE = (By.CSS_SELECTOR, ".body > div:nth-child(1) .name")
    BUTTON_CHANGE_PASSWORD = (By.CSS_SELECTOR, ".body > div:nth-child(2) .name")

    CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, ".form-title > div")
    CHANGE_PASSWORD_FORM_TEXT = 'Смена пароля'
    CHANGE_PASSWORD_FORM_BTN_CLOSE = (By.CSS_SELECTOR, "[alt='X']")

    OLD_PASSWORD = (By.CSS_SELECTOR, "#oldPassword")
    OLD_PASSWORD_ERROR = (By.CSS_SELECTOR, "#oldPassword + .error-message")
    NEW_PASSWORD = (By.CSS_SELECTOR, "#newPassword")
    NEW_PASSWORD_ERROR = (By.CSS_SELECTOR, "#newPassword + .error-message")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#confirmPassword")
    CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, "#confirmPassword + .error-message")
    BUTTON_SUBMIT_PASSWORD = (By.CSS_SELECTOR, "[type='submit']")
    PASSWORD_CHANGED_SUCCESSFULLY = (By.CSS_SELECTOR, ".body > .body-title")
    PASSWORD_CHANGED_SUCCESSFULLY_TEXT = 'Пароль успешно изменен!'
    
    CHANGE_PHONE_FORM = (By.CSS_SELECTOR, ".form-title > div")
    CHANGE_PHONE_FORM_TEXT = 'Введите новый номер'
    CHANGE_PHONE_FORM_BTN_CLOSE = (By.CSS_SELECTOR, "[alt='X']")

    PHONE = (By.CSS_SELECTOR, "[name='phone']")
    PHONE_ERROR = (By.CSS_SELECTOR, ".error-message")
    BUTTON_SUBMIT_PHONE = (By.CSS_SELECTOR, "[type='submit']")
    BUTTON_SUBMIT_PHONE_DISABLED = (By.CSS_SELECTOR, "[disabled='disabled']")
    PHONE_CHANGED_SUCCESSFULLY = (By.CSS_SELECTOR, ".body > .body-title")
    PHONE_CHANGED_SUCCESSFULLY_TEXT = 'Номер телефона успешно изменен!'
    
    

class BasketPageLocators():
    BASKET_TOTAL = (By.CSS_SELECTOR, ".total")
    BASKET_EMPTY = (By.CSS_SELECTOR, ".content #content_inner > p")
