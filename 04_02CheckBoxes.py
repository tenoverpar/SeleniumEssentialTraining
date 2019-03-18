#!/usr/bin/env python

from selenium import webdriver
import time

# Programming in python
# March 16, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# Checkboxes selection

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")
driver.set_page_load_timeout(2)
driver.get("https://formy-project.herokuapp.com/checkbox")
driver.find_element_by_id("checkbox-1").click()
driver.find_element_by_id("checkbox-2").click()
driver.find_element_by_xpath('//*[@id="checkbox-3"]').click()


time.sleep(4)
driver.quit()


print("Test Completed Successfully")
