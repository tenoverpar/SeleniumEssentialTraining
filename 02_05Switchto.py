#!/usr/bin/env python

from selenium import webdriver
import time

# Programming in python
# March 16, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# Stitch between 2 windows

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")
driver.set_page_load_timeout(2)
driver.get("https://formy-project.herokuapp.com/switch-window")

window_before = driver.window_handles[0]
print(window_before)
driver.find_element_by_id("new-tab-button").click()
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
print(window_after)
driver.switch_to_window(window_before)


time.sleep(4)
driver.quit()


print("Test Completed Successfully")
