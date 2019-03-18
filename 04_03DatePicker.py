#!/usr/bin/env python

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Programming in python
# March 18, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# Date Picker

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")
driver.set_page_load_timeout(2)
driver.get("https://formy-project.herokuapp.com/datepicker")
driver.find_element_by_id("datepicker").send_keys("03/03/2020")
driver.find_element_by_id("datepicker").send_keys(Keys.RETURN)


time.sleep(4)
driver.quit()

print("Test Completed Successfully")
