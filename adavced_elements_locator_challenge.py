import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

adv = webdriver.Edge(executable_path='C:\drivers\edgedriver_win64\msedgedriver')
adv.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# 1. Dynamic dropdown - select value 'United States(US)' from the dynamic dropdown
adv.find_element_by_css_selector("input[class='inputs ui-autocomplete-input']").send_keys("United")
time.sleep(2)
list_elements = adv.find_elements_by_css_selector("ul[id = 'ui-id-1'] li")
for element in list_elements:
    if element.text == 'United States (USA)':
        element.click()
        break
print("1 passed.")

# 2. Javascript alert - Enter name in the textbox, validate same name is there in the alert message, click on OK button in alert box, validate if the textbox is empty again
myname = "Rupsha"
adv.find_element_by_id("name").send_keys(myname)
adv.find_element_by_id("alertbtn").click()
alert_box = adv.switch_to.alert
assert myname in alert_box.text
alert_box.accept()
assert len(adv.find_element_by_id("name").text)==0
print("2 passed..")

# 3. Radio button and checkbox - In the radio button, select the 2nd option. In checkbox, first select all the options, then deselect last one and print the text of the deselected option
radio_elements = adv.find_elements_by_css_selector("input[type='radio']")
radio_elements[1].click()

checkbox_elements = adv.find_elements_by_css_selector("input[type$='checkbox']")
for element in checkbox_elements:
    element.click()
checkbox_elements[-1].click()
assert not checkbox_elements[-1].is_selected()
print("Checkbox option selected:", checkbox_elements[-1].get_property("value"))
print("3 passed...")

# 4. Open new window and new tab -- click on the button to open the new tab or window and grab a text from there
adv.find_element_by_css_selector("a[id='opentab']").click()
adv.switch_to.window(adv.window_handles[1]) # to define which window the control should go, the window_handles list is used.
print("Title of new tab is", adv.title, end='\n')
adv.close()
adv.switch_to.window(adv.window_handles[0])

adv.find_element_by_css_selector("button[id='openwindow']").click()
adv.switch_to.window(adv.window_handles[1])
adv.find_element_by_css_selector("a[class='btn btn-primary']").click()
print(adv.find_element_by_css_selector("h2 span strong").text)
adv.close()
adv.switch_to.window(adv.window_handles[0])
print("4 passed....")

# 5. iframe - Go to the iframe on the page, click on an item and come back to the original window
adv.switch_to.frame("courses-iframe") #The frame for the control to travel to can be provided by it's mame, id or index number. I used id here
print(adv.find_element_by_css_selector("h2 span strong").text)
adv.find_element_by_xpath("//a[@href='#/consulting']//div[@class='services-style-one']//div[@class='inner-box']//a[@class='arrow-box']//span[@class='fa fa-angle-right']").click()
adv.switch_to.default_content()
print("5 passed.....")

# 6. Mouse hover - Click on one of the items in the list from hover, that will reload the page
MyActor = ActionChains(adv) # to perform any chaining action, this class needs to be used
MyActor.move_to_element(adv.find_element_by_css_selector("button[id='mousehover']")).perform()
child_element = adv.find_element_by_xpath("//a[normalize-space()='Reload']")
MyActor.click(child_element).perform() #here normal driver class click could also be used, since the element is already on the dom.
print("6 passed......")

# 7. Hide-Show elements - Check first whether the element is present, then hide it, then check whether it's no more visible
assert adv.find_element_by_css_selector("input[id='displayed-text']").is_displayed()
adv.find_element_by_css_selector("input[id='hide-textbox']").click()
assert not adv.find_element_by_css_selector("input[id='displayed-text']").is_displayed()
print("7 passed.......")

adv.close()