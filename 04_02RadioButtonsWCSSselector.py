#!/usr/bin/env python

from selenium import webdriver
import time

# Programming in python
# March 16, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# Radio Buttons

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")
driver.set_page_load_timeout(2)
driver.get("https://formy-project.herokuapp.com/radiobutton")
driver.find_element_by_id("radio-button-1").click()
driver.find_element_by_css_selector("input[value='option2']").click()
driver.find_element_by_xpath("//html/body/div/div[3]/input").click()


time.sleep(4)
driver.quit()


print("Test Completed Successfully")
