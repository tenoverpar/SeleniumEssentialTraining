#!/usr/bin/env python

from selenium import webdriver
import time

# Programming in python
# March 18, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# Dropdown menu

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")
driver.set_page_load_timeout(2)
driver.get("https://formy-project.herokuapp.com/dropdown")
driver.find_element_by_id("dropdownMenuButton").click()
driver.find_element_by_id("autocomplete").click()

time.sleep(4)
driver.quit()

print("Test Completed Successfully")
