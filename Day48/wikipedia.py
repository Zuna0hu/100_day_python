from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a driver for Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# stat_element = driver.find_element(By.CSS_SELECTOR, value="#articlecount a") # there are two a elements, this will select the first one
stat_element = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
stat = stat_element.text

print(stat)

# quit the entire browser
driver.quit()