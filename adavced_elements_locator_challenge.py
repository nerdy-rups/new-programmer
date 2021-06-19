import time
from selenium import webdriver

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

# 2. Javascript alert - Enter name in the textbox, validate same name is there in the alert message, click on OK button in alert box, validate if the textbox is empty again



# 3. Radio button and checkbox - In the radio button, select the 2nd option. In checkbox, first select all the options, then deselect last one and print the text of the deselected option
radio_elements = adv.find_elements_by_css_selector("input[type='radio']")
radio_elements[1].click()

checkbox_elements = adv.find_elements_by_css_selector("input[type$='checkbox']")
for element in checkbox_elements:
    element.click()
checkbox_elements[-1].click()
assert not checkbox_elements[-1].is_selected()
print("Checkbox option selected:", checkbox_elements[-1].get_property("value"))

# 4. Datepicker

adv.close()