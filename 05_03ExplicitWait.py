#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Programming in python
# March 18, 2019
# Lynda.com -Selenium-tutorials
# Tracy Allen - git repo https://github.com/tenoverpar/
# autocomplete Explicit wait

driver = webdriver.Chrome("/home/tennison/Selenium/drivers/chromedriver")
# driver.set_page_load_timeout(10)
driver.get("https://formy-project.herokuapp.com/autocomplete")
driver.find_element_by_id("autocomplete").send_keys("1555 Park Blvd, Palo Alto, CA")

try:
    element = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "pac-item"))
        )
finally:
    driver.quit()
    print("Test Completed Successfully")
