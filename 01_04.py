#!/usr/bin/env python

from selenium import webdriver

# Programming in python
# March 16, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")

driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Cheese!")
driver.find_element_by_name("btnK").click()
driver.quit()
