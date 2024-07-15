import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from TEST1.SUBTEST1.LOGIN_PAGE import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    #yield the webdriver instance
    yield driver

    #close the webdriver
    driver.quit()

def test_login(driver):
    login_page=LoginPage(driver)
    login_page.open_page("https://web.khalti.com/#/")
    time.sleep(1)
    login_page.enter_email("9861287129")
    time.sleep(1)
    login_page.enter_password("PABITRA@11")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)


    print("congrats!!!")

