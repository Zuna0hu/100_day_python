from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# this file will automate filling out forms and clicking buttons

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a driver for Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# how to click
# element_to_click = driver.find_element(By. ...)
# element_to_click.click()

# how to send keyboard input
# find the element
# element_to_send.send_keys("Text", Keys.ENTER, Keys.TAB ...)


# quit the entire browser
driver.quit()