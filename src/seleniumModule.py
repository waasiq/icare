import time
from selenium import webdriver
#! Uncomment if necessary
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

SADNESS_PAGE = "https://www.youtube.com/watch?v=ur48jVNNlKk&aby"
SMILE_PAGE = "https://www.youtube.com/watch?v=ht9YrIcr0ck&ab_channel=Johnwaller"
WINK_PAGE = "https://www.youtube.com/watch?v=-cC_UrCFg5w&ab_channel=Danapan"
ANGER_PAGE = "https://www.youtube.com/watch?v=lFcSrYw-ARY" 
SHOCK_PAGE = "https://www.youtube.com/watch?v=Cm_OZgjXhVs&ab_channel=TheOutcome"
GOOD_SOUP = "https://www.youtube.com/watch?v=gkXzeZ0KE5Q"
FINGER_FLIP = "https://www.youtube.com/watch?v=XtDk7yc4VV8"

driver = webdriver.Chrome()
driver.maximize_window()

    #*-> 1. Anger
    #*-> 2. Sadness
    #*-> 3. Smile
    #*-> 4. Shock
    #*-> 5. Wink


def anger(driver):
    driver.get(ANGER_PAGE)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
    time.sleep(8)
    driver.close()
  

def sadness(driver):
    driver.get(SADNESS_PAGE)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
    time.sleep(8)
    driver.close()
  
    
def smile(driver):
    driver.get(SMILE_PAGE)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
    time.sleep(8)
    driver.close()
  

def shock(driver):
    driver.get(SHOCK_PAGE)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
    time.sleep(8)
    driver.close()
  

def wink(driver):
    driver.get(WINK_PAGE)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
    time.sleep(8)
    driver.close()
  

def good_soup(driver):
    driver.get(GOOD_SOUP)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
    time.sleep(8)
    driver.close()
  


def finger_flip(driver):
    driver.get(FINGER_FLIP)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
    time.sleep(7)
    driver.close()
    print("\n\nFlip the finger.")


def main():    
    pass


if __name__ == "__main__":
    main()