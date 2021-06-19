import time
from selenium import webdriver
from selenium.webdriver import ActionChains

# Double click - Double click on the element, open the alert and close it.
DCCC = webdriver.Edge(executable_path='C:\drivers\edgedriver_win64\msedgedriver')
DCCC.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
Actress = ActionChains(DCCC)
Actress.move_to_element(DCCC.find_element_by_id("double-click")).perform()
Actress.double_click().perform()
new_alert = DCCC.switch_to.alert
new_alert.accept()

time.sleep(2)

# Context click - Context click on the prompt element, open the alert, enter some text and dismiss the alert.
Actress2 = ActionChains(DCCC) #same actionchain object CANNOT be used for 2 different actions.
Actress2.context_click(DCCC.find_element_by_name("prompt")).perform()
Actress2.click(DCCC.find_element_by_name("prompt")).perform()
second_alert = DCCC.switch_to.alert
second_alert.send_keys("My shoe is Japanese")
second_alert.accept()

DCCC.close()
