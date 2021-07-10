"""Scenario: Go to the site, use all the simple fields in the page, click on Submit button and verify the success message"""

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_xpath("//div[@class='form-group'][1]/input").send_keys("Rupsha")
driver.find_element_by_xpath("//input[@name='email']").send_keys("rupsha@email.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("abcde")
gender = Select(driver.find_element_by_id("exampleFormControlSelect1"))
gender.select_by_visible_text("Female")
driver.find_element_by_xpath("//input[@value='Submit']").click()
success_message = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
assert "Success" in success_message

driver.close()