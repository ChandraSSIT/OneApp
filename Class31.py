import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

time.sleep(3)
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
# driver.find_element(By.XPATH,"//div[@class='form_group'][1]/input").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.CLASS_NAME,"submit-button.btn_action").click()
time.sleep(3)

# //dropdown
selectobj = Select(driver.find_element(By.CSS_SELECTOR,".product_sort_container"));
# print(selectobj.options)
selectobj.select_by_visible_text("Price (low to high)")
time.sleep(5)
selectobj = Select(driver.find_element(By.CSS_SELECTOR,".product_sort_container"));
selectobj.select_by_index(1)
time.sleep(5)
selectobj = Select(driver.find_element(By.CSS_SELECTOR,".product_sort_container"));
selectobj.select_by_value("za")

# Check boxes
# Radio buttons
# Wait concepts

driver.get("https://demo.guru99.com/test/radio.html")
driver.find_element(By.XPATH,"//*[@type='radio'][2]").click()

time.sleep(2)
driver.find_element(By.XPATH,"//*[@type='checkbox'][2]").click()
driver.find_element(By.XPATH,"//*[@type='checkbox'][3]").click()