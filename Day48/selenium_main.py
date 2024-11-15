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

# how to find one pair of date and location
# time1 = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time')
# print(time1.get_attribute("datetime")[:10])
# place1 = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/a')
# print(place1.text)

events_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events_locs = driver.find_elements(By.CSS_SELECTOR, value=".event-widget a")
events = {}

for n in range(len(events_dates)):
    events[n] = {
        "date": events_dates[n].get_attribute("datetime")[:10],
        "location": events_locs[n].text
    }

print(events)

# to close the browser automatically
# driver.close() # close the tab only
driver.quit() # quit the entire browser 