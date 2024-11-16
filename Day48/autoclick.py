from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# this file will automate filling out forms and clicking buttons

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a driver for Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# how to click
# element_to_click = driver.find_element(By. ...)
# element_to_click.click()

# how to send keyboard input
# find the element
# element_to_send.send_keys("Text", Keys.ENTER, Keys.TAB ...)

# get the elements
fname_element = driver.find_element(By.NAME, value="fName")
lname_element = driver.find_element(By.NAME, value="lName")
email_element = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CLASS_NAME, value="btn")

fname_element.send_keys("Jotaro")

lname_element.send_keys("Kujo")

email_element.send_keys("fake_email@fakemail.com")

button.click()

# quit the entire browser
# driver.quit()