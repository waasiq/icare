import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/")

driver.find_element_by_xpath('//*[@id="L2AGLb"]/div').click()

driver.find_element_by_name("q").send_keys("github")
time.sleep(2)

driver.close()
print("Done.")