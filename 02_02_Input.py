#!/usr/bin/env python

from selenium import webdriver
import time

# Programming in python
# March 16, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")

driver.set_page_load_timeout(10)
driver.get("https://formy-project.herokuapp.com/keypress")
driver.find_element_by_id("name").click()
driver.find_element_by_id("name").send_keys("Tennison Overpar")
driver.find_element_by_id("button").click()
time.sleep(2)
driver.quit()
# driver.find_element_by_name("btnK").click()
