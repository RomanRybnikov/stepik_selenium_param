import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import *

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button(browser):
    browser.get(link)
    assert browser.find_element(By.XPATH, "//button[@type]"), "Button not found"