from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ec, fr, ru, .....")


@pytest.fixture(scope="function")
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
        options.add_argument('--window-size=1800,1000')
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
