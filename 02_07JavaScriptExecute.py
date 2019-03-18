#!/usr/bin/env python

from selenium import webdriver
import time

# Programming in python
# March 16, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# Handle Java Script execute

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")
driver.set_page_load_timeout(2)
driver.get("https://formy-project.herokuapp.com/modal")
driver.find_element_by_id("modal-button").click()
closebutton = driver.find_element_by_id("close-button")
driver.execute_script("arguments[0].click();", closebutton)


time.sleep(4)
driver.quit()


print("Test Completed Successfully")
