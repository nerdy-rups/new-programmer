import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

ftc = webdriver.Chrome(executable_path='C:\drivers\chromedriver_win32\chromedriver')
ftc.get('https://rahulshettyacademy.com/seleniumPractise/#/')
ftc.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys("BR")
time.sleep(2)

# Test case 1 - Verify the same items which are selected in first page are showing in the second page
result = ftc.find_elements_by_xpath("//div[@class='product-action']/button")
veg_names_page1 = []
for r in result:
    veg_names_page1.append(r.find_element_by_xpath("parent::div/parent::div/h4").text)
    r.click()
ftc.find_element_by_xpath("//img[@alt='Cart']").click()
ftc.find_element_by_xpath("//button[normalize-space()='PROCEED TO CHECKOUT']").click()

time.sleep(2) # this pause in execution is required because when the page is loaded, the 'selected_items' list already gets and stores the blank values before the actual values are loaded.

veg_names_page2 = []
selected_items = ftc.find_elements_by_xpath("//p[@class='product-name']")
for item in selected_items:
    veg_names_page2.append(item.text)

assert veg_names_page2 == veg_names_page1
print("First test case pass")


#Test case 2 - Verify the sum of price of all items on the page is equal to the sum displayed as Total
sum_of_items = 0
for i in ftc.find_elements_by_xpath("//tbody/tr/td[5]"):
    sum_of_items+=int(i.text)
sum_displayed = ftc.find_element_by_xpath("//span[@class='totAmt']").text
assert int(sum_displayed) == sum_of_items
print("Second test case pass")


#Test case 3 - Verify that the price after giving discount is less than the original price
price_before = int((ftc.find_element_by_css_selector("span.totAmt")).text)

ftc.find_element_by_css_selector("input.promoCode").clear()
ftc.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
ftc.find_element_by_css_selector(("button.promoBtn")).click()

waiter = WebDriverWait(ftc, 10)
waiter.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
#here this wait is needed for the script to understand that the effect of promo code application is successful

price_after = float(ftc.find_element_by_css_selector("span.discountAmt").text)
assert price_after < price_before
print("Third test case pass")
ftc.close()