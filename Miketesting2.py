import time
from sqlite3 import Time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.saucedemo.com/")

driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(5)

#select 5 items
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()
time.sleep(2)

#unselect items 1,3 and 5
driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-backpack']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-bolt-t-shirt']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-onesie']").click()

# #continue shopping
# driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()
# time.sleep(3)

#add two more items
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()
time.sleep(5)

#checkout button
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='checkout']").click()
time.sleep(5)

driver.quit()

# driver.find_element(By.ID, "logout-button").click()
# driver.quit()

#//*[@id="shopping_cart_container"]/a

