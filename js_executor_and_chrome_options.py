from selenium import webdriver

"""Chrome options - Open a non-secure site in headless mode and get it's title"""
CO = webdriver.ChromeOptions()
CO.add_argument("--headless")
CO.add_argument("--ignore-certificate-errors")
#my_driver = webdriver.Chrome(executable_path='C:\drivers\chromedriver_win32\chromedriver.exe', options=CO)
#my_driver.get("http://neverssl.com/")
#print(my_driver.title)
print("test pass")


"""js executor - Go to the angular practice page, enter some text in the textfield, then display the same text using js 
script executor. Scroll to the bottom of the page and click the button, both using js"""

my_driver2 = webdriver.Chrome(executable_path='C:\drivers\chromedriver_win32\chromedriver.exe')
my_driver2.maximize_window()
my_driver2.get("https://rahulshettyacademy.com/angularpractice/")
my_driver2.find_element_by_name("email").send_keys("sbcde@email.com")
value_entered = return(my_driver2.execute_script())
print(value_entered)

