# UI(User interface) Automation
# selenium (Page object model framework) framework
# Page is nothing but webpage(html page)
# DOM (Document object Model) element
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Locators
# ID
# Name
# ClassName
# XPath
# CSS Selector Path

# ID
# time.sleep(3)
# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# time.sleep(3)
# driver.find_element(By.ID,"password").send_keys("secret_sauce")
# time.sleep(3)
# driver.find_element(By.ID,"login-button").click()
# time.sleep(5)

# Name
# time.sleep(3)
# driver.find_element(By.NAME,"user-name").send_keys("standard_user")
# time.sleep(3)
# driver.find_element(By.NAME,"password").send_keys("secret_sauce")
# time.sleep(3)
# driver.find_element(By.NAME,"login-button").click()
# time.sleep(5)

# Class Name
time.sleep(3)
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
# driver.find_element(By.XPATH,"//div[@class='form_group'][1]/input").send_keys("standard_user")
time.sleep(3)
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"submit-button.btn_action").click()
# time.sleep(5)



#Css Selector

driver.find_element(By.CSS_SELECTOR,"div.inventory_list div.inventory_item:nth-child(1) div.inventory_item_description div.pricebar button").click()




# XPath
# Absolute XPath => It will find the element from root of the html to till element , we will use single slash
# /html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[1]/input
# Relative XPath => we will try to find element based on some parent level or relative to that element
#  we will use //
# //tagname[@attribute = 'value']
# attribute name => Id,Name,class,text()
# //div[@class='form_group'][1]/input

# alert
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.find_element(By.XPATH,"//input[@value='Alert']").click()

time.sleep(5)
driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()  # cancel

# Navigation commands
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)

# screen shot

driver.save_screenshot('testimage.jpg')

# dropdown



# Actionchains


driver.close() #to close current tab/window
# driver.quit() # to close complete browser