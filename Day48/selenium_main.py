from selenium import webdriver

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create a driver for Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")