from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.XPATH, "//button[@type]"), "Button not found"