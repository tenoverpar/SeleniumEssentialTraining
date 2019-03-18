#!/usr/bin/env python
from selenium import webdriver
# from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.common.keys import Keys

# Programming in python
# March 16, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/


driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")

driver.set_page_load_timeout(10)
driver.get("https://formy-project.herokuapp.com/autocomplete")
driver.find_element_by_id("autocomplete").send_keys("1555 Park Blvd, Palo Alto, CA")
time.sleep(2)
driver.find_element_by_class_name("pac-item").click()
time.sleep(4)


driver.maximize_window()
driver.refresh()
time.sleep(4)
driver.quit()


print("Test Completed Successfully")
