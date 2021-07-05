import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browserName", action = "store", default = "Chrome", help ="Enter the browser name")


@pytest.fixture(scope="class")
def Setup(request): # request is an instance for the fixture that is auto built
    SelectedBrowser = request.config.getoption("browserName")
    if SelectedBrowser == "Chrome":
        Driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver")
    elif SelectedBrowser == "Edge":
        Driver = webdriver.Edge(executable_path = "C:\drivers\edgedriver_win64\msedgedriver")
    Driver.get("https://rahulshettyacademy.com/angularpractice/")
    Driver.maximize_window()
    request.cls.myDriver = Driver #this line is actually sending the webdriver instance created here to the class calling it.
    yield
    Driver.close()