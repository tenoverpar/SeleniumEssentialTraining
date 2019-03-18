#!/usr/bin/env python
from selenium import webdriver
import time

# Programming in python
# March 16, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")

driver.set_page_load_timeout(2)
driver.get("https://formy-project.herokuapp.com/scroll")

driver.find_element_by_id("name").send_keys("Tennison Overpar")

driver.find_element_by_id("date").send_keys("01/01/2020")

# driver.find_element_by_id("name").send_keys("Tennison Overpar")
time.sleep(4)
driver.quit()


print("Test Completed Successfully")
