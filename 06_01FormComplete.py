#!/usr/bin/env python
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Programming in python
# March 18, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# Put is all together Form completion

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")

driver.set_page_load_timeout(5)
driver.get("https://formy-project.herokuapp.com/form")
driver.find_element_by_id("first-name").send_keys("Tennison")
driver.find_element_by_id("last-name").send_keys("OverPar")
driver.find_element_by_id("job-title").send_keys("QA Specialist")
driver.find_element_by_id("radio-button-2").click()
driver.find_element_by_id("checkbox-1").click()
# Work on select menu here
driver.find_element_by_id("select-menu")
driver.find_element_by_css_selector("option[value='4']").click()
# date picker
driver.find_element_by_id("datepicker").send_keys("03/03/2020")
driver.find_element_by_id("datepicker").send_keys(Keys.RETURN)
# Submit button add the . to indicate each class
driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()


time.sleep(4)
driver.quit()


print("Test Completed Successfully")
