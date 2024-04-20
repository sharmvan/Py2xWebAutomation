from selenium import webdriver  # Selenium is a framework. it's basically a library that we have downloaded and
# in the selenium we have webdriver. that's why we returned from selenium import webdriver. In the webdriver, we have chrome.
import time
import pytest


@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()  # POST request / Create the session
    driver.get("https://app.vwo.com")  # GET request to URL parameters
    print(driver.title)  # It Returns the title of the current page.
    # print(driver.page_source)
    print(driver.session_id)  # A unique id which is created when you have started a browser.
    driver.maximize_window()
    assert driver.title == "Login - VWO"  # We can add assertions also as we are using pytest
