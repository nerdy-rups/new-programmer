import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("Setup")
class baseClass:

    def verifyLinkPresence(self, linkname):
        WebDriverWait(self.myDriver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, linkname)))
    """Work of the above method: Take the linkname of the intended element at runtime, where this baseClass is being used and use it
     as a normal explicit wait. Since this method is part of the class that is using the Setup fixture, it takes the same driver name."""

    @pytest.fixture(
        params=[("Rupsha", "rupsha@email.com", "abcde", "Female"), ("Rahul", "rahul@email.com", "fghij", "Male")])
    def getData(self, request):
        return request.param