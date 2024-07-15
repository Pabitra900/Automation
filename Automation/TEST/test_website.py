import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_google_search():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://google.com.np")

    search_box = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
    search_box.send_keys("mindrisers.com.np")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Click on the first link
    first_link = driver.find_element(By.XPATH,
                                     "//a[@href='https://mindrisers.com.np/']//h3[contains(text(),'Best IT Training Institute in kathmandu, Nepal | M')]")
    first_link.click()
    time.sleep(5)
    print("Congrats!! pytest completed successfully")

    # Open the website directly
    website_url = 'https://mindrisers.com.np/'
    driver.get(website_url)

    # Maximize the window
    driver.maximize_window()
    time.sleep(3)

    # Calculate the height of page using JavaScript
    page_height = driver.execute_script("return document.body.scrollHeight")

    # Scroll down the webpage using JavaScript
    scroll_speed = 1000
    scroll_iterations = int(page_height / scroll_speed)
    for i in range(scroll_iterations + 1):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(1)

    # Open the contact page
    website_url = "https://mindrisers.com.np/contact-us"
    driver.get(website_url)
    time.sleep(5)
    driver.maximize_window()
    time.sleep(3)

    # Locate the attributes
    Name = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    Email = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
    phone_number = driver.find_element(By.XPATH, "//input[@placeholder='Phone']")
    subject = driver.find_element(By.XPATH, "//input[@placeholder='Subject']")
    Any_queries = driver.find_element(By.XPATH, "//textarea[@placeholder='Queries']")

    # Fill the contents with your data
    Name.send_keys("Pabitra")
    Email.send_keys("pabitra@gmail.com")
    phone_number.send_keys("0987456798")
    subject.send_keys("English")
    Any_queries.send_keys("I AM TESTING THIS")
    time.sleep(4)

    # Extract the website title
    website_title = driver.title
    print(f"Website title: {website_title}")

    # Close the browser
    driver.quit()

    print("Congratulations for successful code execution")


if __name__ == "__main__":
    test_google_search()
