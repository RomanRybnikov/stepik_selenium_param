import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}

supported_languages = {
    'Русский': 'ru',
    'British English': 'en-gb',
    'español': 'es',
    'Українська': 'uk'
    }

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru/eng")

    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome/firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    language_default = "ru"

    if browser_name not in supported_browsers:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    if language in supported_languages.values():
        if  browser_name == 'chrome':
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            browser = webdriver.Chrome(options=options)

        elif browser_name == 'firefox':
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language)
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language_default})
            browser = webdriver.Chrome(options=options)

    yield browser
    print("\nQuit browser..")
    # time.sleep(3)
    browser.quit()