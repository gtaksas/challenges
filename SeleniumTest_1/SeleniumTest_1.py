#Selenium Test #1
#https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("kukuccs")
search.send_keys(Keys.RETURN)

link = driver.find_element_by_link_text("Képek")
link.click()

time.sleep(2)

driver.quit()