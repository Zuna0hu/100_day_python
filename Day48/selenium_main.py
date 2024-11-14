from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a driver for Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# you can use id, name, class, css selector and xpath to find element

# search_bar = driver.find_element(By.NAME), value='q')
# print(search_bar.get_attributes("placeholder"))
# find_element(By.ID), By.CSS_SELECTOR, By.XPATH ...

time1 = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time')
print(time1.get_attribute("datetime")[:10])
place1 = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/a')
print(place1.text)


# to close the browser automatically
# driver.close() # close the tab only
driver.quit() # quit the entire browser 