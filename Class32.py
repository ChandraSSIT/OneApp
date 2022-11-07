import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()


# wait = WebDriverWait(driver,3)
# wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/div/div/div[4]/a/div[1]/div")))

actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/div/div/div[4]/a/div[1]")).perform()
time.sleep(5)
actions.move_to_element(driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/div/div/div[4]/a/div[2]/div[2]/div[2]/div/div/div[1]/a[2]")).click().perform()
time.sleep(10)
# actions.double_click(element).perform()
# actions.context_click(element).perform()

driver.execute_script("window.scrollBy(0,800)","")

time.sleep(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.close()


# Wait concept
# Implicit wait
# Explicit wait

# wait = WebDriverWait(driver,10)
# wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/div/div/div[4]/a/div[1]/div")))