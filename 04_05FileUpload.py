#!/usr/bin/env python

from selenium import webdriver
import time

# Programming in python
# March 18, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# File Upload

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")
driver.set_page_load_timeout(2)
driver.get("https://formy-project.herokuapp.com/fileupload")
driver.find_element_by_id("file-upload-field").send_keys("file-to-upload.png")


time.sleep(4)
driver.quit()

print("Test Completed Successfully")
