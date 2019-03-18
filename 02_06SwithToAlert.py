#!/usr/bin/env python

from selenium import webdriver
import time

# Programming in python
# March 16, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# Handle Alert Button

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")
driver.set_page_load_timeout(2)
driver.get("https://formy-project.herokuapp.com/switch-window")
driver.find_element_by_id("alert-button").click()
driver.switch_to_alert().accept()

time.sleep(4)
driver.quit()


print("Test Completed Successfully")
