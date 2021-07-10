from selenium.webdriver.common.by import By

class ShopPage:
    phone_areas = (By.XPATH, "//body//app-root//app-card")
    checkout_link = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def __init__(self, shopDriver):
        self.driver = shopDriver

    def phone_area(self):
        return self.driver.find_elements(*ShopPage.phone_areas)

    def phone_selection(self):
        global phoneSelected
        phone_areas = ShopPage.phone_area(self)
        for area in phone_areas:
            if area.find_element_by_xpath("div/div[@class='card-body']/h4/a").text == 'Nokia Edge':
                phoneSelected = area.find_element_by_xpath("div/div[@class='card-body']/h4/a").text
        return phoneSelected

    def click_checkout(self):
        return self.driver.find_element(*ShopPage.checkout_link)
