from selenium import webdriver
import pytest
import time
#from .test_login_page import LogIn
from .pages.login_page import LoginPage
from .data import *
#import uuid
#import allure

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ec, fr, ru, .....")


@pytest.fixture(scope="session") # выполняется перед каждой сессией
#@pytest.fixture(scope="package") 
#@pytest.fixture(scope="module") 
#@pytest.fixture(scope="class") 
#@pytest.fixture(scope="function") # выполняется перед каждой функцией

def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\n** START chrome browser for test **")
        options = webdriver.ChromeOptions()
        options.add_argument('chrome')
#        options.add_argument("--headless") # если запускать без отображения браузера, тогда убрать строку выше options.add_argument('chrome')
        options.add_argument('--start-maximizid')
        options.add_argument('--window-size=1080,1080')
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\n** START firefox browser for test **")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n** QUIT browser **")
    browser.quit()



@pytest.fixture
def login_fixture(browser):
    # авторизация пользователя
    page = LoginPage(browser, '/login')  
    print('===================LogIn()==========================')    
    page.open()
    page.logout_user() # выход из авторизации, если есть авторизация
    page.login_user(*login_password_valid) # авторизация пользователя 
    time.sleep(2)
