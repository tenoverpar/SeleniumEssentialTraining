#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# Programming in python
# March 16, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# Drag and drop

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")
driver.set_page_load_timeout(2)
driver.get("https://formy-project.herokuapp.com/dragdrop")
image = driver.find_element_by_id("image")
box = driver.find_element_by_id("box")
ActionChains(driver).drag_and_drop(image, box).perform()


time.sleep(4)
driver.quit()


print("Test Completed Successfully")
