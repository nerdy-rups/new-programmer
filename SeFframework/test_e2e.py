import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import pytest
from PageObjects.HomePage import HomePage
from PageObjects.ShopPage import ShopPage
from Utilities.BaseClass import baseClass

@pytest.mark.usefixtures("getData")
class TestOne(baseClass):

    def test_firstTestCase(self, getData):
        homepage1 = HomePage(self.myDriver)
        #homepage1.name_entry().send_keys("Rupsha")
        homepage1.name_entry().send_keys(getData[0])
        #homepage1.email_entry().send_keys("rupsha@email.com")
        homepage1.email_entry().send_keys(getData[1])
        #homepage1.password_entry().send_keys("abcde")
        homepage1.password_entry().send_keys(getData[2])
        gender_options = homepage1.gender_select()
        #gender_options.select_by_visible_text("Female")
        gender_options.select_by_visible_text(getData[3])
        homepage1.submit_click().click()

        success_message = self.myDriver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
        assert "Success" in success_message
        self.myDriver.refresh()

class TestTwo(baseClass): # <--- keeping this explicitly will cause the browser to close after execution of the first test and reopen for this one.
    def test_secondTestCase(self):
        # Adding item to cart:
        #self.myDriver.find_element_by_link_text("Shop").click()
        homepage = HomePage(self.myDriver)
        homepage.shopLink().click()

        shoppage = ShopPage(self.myDriver)
        phones = shoppage.phone_area()
        print (phones)
        phone_selected = shoppage.phone_selection()
        print(phone_selected)
        price = None
        for phone in phones:
            if phone.find_element_by_xpath("div/div[@class='card-body']/h4/a").text == 'Nokia Edge':
                price = phone.find_element_by_xpath("div/div[@class='card-body']/h5").text
                phone.find_element_by_xpath("div/div[@class='card-footer']/button").click()
                print("Selected:", phone_selected, "priced", price)
                price_refined = price.split('$')
        print(price_refined)
        shoppage.click_checkout().click()

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
        self.myDriver.save_screenshot("test_image.png")



