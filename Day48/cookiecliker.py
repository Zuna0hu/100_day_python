from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a driver for Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# cookie button
cookie_button = driver.find_element(By.ID, value="cookie")
# items
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
# money
money_element = driver.find_element(By.ID, value="money")
# coockies per second
cps_element = driver.find_element(By.ID, value="cps")

# the total amout of time of program
duration = 300   # seconds
# define the internal to perform an action
interval = 10 # seconds
# time to start
start_time = time.time()

print(len(items))
for n in range(-1, -len(items)-1, -1): # -1, -2, .. - -n
    print(items[n].text)

last_checked_time = start_time

while time.time() - start_time < duration: 
    # click
    cookie_button.click()
    # if (time.time() - start_time) % interval < 0.1: # because time.time() is float, this condition is rarely met
    if time.time() - last_checked_time >= interval:
        print(f"Time elapsed: {time.time() - last_checked_time}, Interval: {interval}")
        last_checked_time = time.time()
        # check if the items are purchasable
        items = driver.find_elements(By.CSS_SELECTOR, value="#store div") # test
        
        for n in range(-1, -len(items)-1, -1): # -1, -2, .. - -n
            try:
                # if it is clickable, click it
                items[n].click()
                print(f"click {items[n].text}")
            except Exception:
                pass  # Silently ignore any exception

# print the total amount of money
print(f"total money: {money_element.text}")
# cookies per second
print(f"cookies per second: {cps_element.text}")




# quit the entire browser
driver.quit()