#!/usr/bin/env python
from selenium import webdriver
import time

# Programming in python
# March 18, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# autocomplete Implicit wait


driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")

driver.set_page_load_timeout(10)
driver.get("https://formy-project.herokuapp.com/autocomplete")
driver.find_element_by_id("autocomplete").send_keys("1555 Park Blvd, Palo Alto, CA")
time.sleep(5)

driver.find_element_by_class_name("pac-item").click()
time.sleep(4)

driver.quit()


print("Test Completed Successfully")
