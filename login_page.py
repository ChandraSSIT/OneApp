import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def login_page(username,password):

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    driver.find_element(By.NAME, "user-name").send_keys(username)
    # driver.find_element(By.XPATH,"//div[@class='form_group'][1]/input").send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "submit-button.btn_action").click()
    time.sleep(5)
    return driver.current_url