#login_pages

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.email_textbox=(By.ID,"email")
        self.password_textbox=(By.NAME,"password")
        self.login_button=(By.XPATH,"//button[normalize-space()='Login']")


    def open_page(self,url):
        self.driver.get(url)

    def enter_email(self,email):
        self.driver.find_element(*(By.XPATH,"//input[@name='id']")).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*(By.XPATH, "//input[@name='password']")).send_keys(password)
    def click_login(self):
        self.driver.find_element(*(By.XPATH,"//button[normalize-space()='Login']")).click()



