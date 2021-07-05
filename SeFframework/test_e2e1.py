import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import baseClass


class TestOne(baseClass):

    def test_firstTestCase(self):
        # Adding item to cart:
        #self.myDriver.find_element_by_link_text("Shop").click()
        homepage = HomePage(self.myDriver)
        homepage.shopLink()
        phones = self.myDriver.find_elements_by_xpath("//body//app-root//app-card")
        phone_selected = None
        price = None
        for phone in phones:
            if phone.find_element_by_xpath("div/div[@class='card-body']/h4/a").text == 'Nokia Edge':
                phone_selected = phone.find_element_by_xpath("div/div[@class='card-body']/h4/a").text
                price = phone.find_element_by_xpath("div/div[@class='card-body']/h5").text
                phone.find_element_by_xpath("div/div[@class='card-footer']/button").click()
                print("Selected:", phone_selected, "priced", price)
                price_refined = price.split('$')
        print(price_refined)

        # Checkout:
        self.myDriver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

        # Checkout page:
        waiter = WebDriverWait(self.myDriver, 5)
        waiter.until(expected_conditions.presence_of_element_located((By.XPATH, "//td/div[@class='media']")))
        item_in_checkout = self.myDriver.find_element_by_link_text("Nokia Edge").text
        price_in_checkout = (self.myDriver.find_element_by_xpath("//tbody/tr[1]/td[3]/strong").text).split(' ')
        print((price_in_checkout))
        if item_in_checkout == phone_selected:
            print("Test case pass. Same item present")
        if round(float(price_refined[1]) * 2601.04, 0) == round(float(price_in_checkout[1]), 0):
            print("Test case pass. Price matching")

        self.myDriver.find_element_by_css_selector("button[class='btn btn-success']").click()

        # t&c page:
        self.verifyLinkPresence("#country")

        self.myDriver.find_element_by_css_selector("#country").send_keys("Ind")
        time.sleep(5)
        countries = self.myDriver.find_elements_by_xpath("//div[@class='suggestions']/ul/li/a")
        for country in countries:
            if country.text == "India":
                country.click()
                break
        self.myDriver.find_element_by_xpath("//label[@for='checkbox2']").click()
        self.myDriver.find_element_by_xpath("//input[@value='Purchase']").click()
        waiter.until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "div[class$='alert alert-success alert-dismissible'] strong")))
        if "Success" in self.myDriver.find_element_by_css_selector(
                "div[class$='alert alert-success alert-dismissible'] strong").text:
            print("Test case pass. Item booked")
        self.myDriver.save_screenshot("test_image.png")  # If the file already exists, it is overwritten



