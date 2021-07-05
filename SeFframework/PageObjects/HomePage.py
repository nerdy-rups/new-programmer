from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    shop_link = (By.LINK_TEXT, "Shop")

    def __init__(self, ddrriivveerr):
        self.driver = ddrriivveerr

    def shopLink(self):
        print(self.driver.find_element(*HomePage.shop_link))

#homepage = HomePage()
#homepage.shop_link()