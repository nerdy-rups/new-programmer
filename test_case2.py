"""Test case: Go to https://rahulshettyacademy.com/seleniumPractise/#/, enter some values in the search box and, add the resultant 
items to cart, go to cart page, apply promo code and verify the promo code messages"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

tc3 = webdriver.Chrome(executable_path='C:\drivers\chromedriver_win32\chromedriver')
tc3.get('https://rahulshettyacademy.com/seleniumPractise/#/')
#implicit wait for 5 seconds applied
tc3.implicitly_wait(5)
tc3.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(3)
"""Above sleep is required to pause the python execution at this point because otherwise the next coded steps take place
before the earlier action is complete. Eg: Consuming all the products in unfiltered state on page"""
result = tc3.find_elements_by_xpath("//div[@class='product-action']/button")
for r in result:
    r.click()
tc3.find_element_by_xpath("//img[@alt='Cart']").click()
tc3.find_element_by_xpath("//button[normalize-space()='PROCEED TO CHECKOUT']").click()

tc3.find_element_by_css_selector("input.promoCode").send_keys("test value")
tc3.find_element_by_css_selector("button.promoBtn").click()

#explicit wait application - this will make the particular step or action to wait for the specified time or action, whichever is earlier.
waiter = WebDriverWait(tc3, 10)
waiter.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(tc3.find_element_by_css_selector("span.promoInfo").text)

tc3.find_element_by_css_selector("input.promoCode").clear()
tc3.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
tc3.find_element_by_css_selector("button.promoBtn").click()

time.sleep(6)
if "Code applied" in tc3.find_element_by_css_selector("span.promoInfo").text:
    tc3.close()
    print("Test case pass")
