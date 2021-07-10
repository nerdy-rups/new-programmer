from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest

class HomePage:

    shop_link = (By.LINK_TEXT, "Shop")
    name_field = (By.XPATH, "//div[@class='form-group'][1]/input")
    email_field = (By.XPATH, "//input[@name='email']")
    password_field = (By.XPATH, "//input[@type='password']")
    gender_field = (By.ID, "exampleFormControlSelect1")
    submit_button = (By.XPATH, "//input[@value='Submit']")

    def __init__(self, ddrriivveerr):
        self.driver = ddrriivveerr

    def shopLink(self):
        return self.driver.find_element(*HomePage.shop_link)

    def name_entry(self):
        return self.driver.find_element(*HomePage.name_field)

    def email_entry(self):
        return self.driver.find_element(*HomePage.email_field)

    def password_entry(self):
        return self.driver.find_element(*HomePage.password_field)

    def gender_select(self):
        return Select(self.driver.find_element(*HomePage.gender_field)) #small trick to handle the dropdown

    def submit_click(self):
        return self.driver.find_element(*HomePage.submit_button)

    """"@pytest.fixture(
        params=[("Rupsha", "rupsha@email.com", "abcde", "Female"), ("Rahul", "rahul@email.com", "fghij", "Male")])
    def getData(self, request):
        return request.param"""