import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
#! Uncomment if necessary
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

SADNESS_PAGE = ""
SMILE_PAGE = ""
WINK_PAGE = ""
ANGER_PAGE = ""
GOOD_SOUP = "https://www.youtube.com/watch?v=gkXzeZ0KE5Q"
FINGER_FLIP = "https://www.youtube.com/watch?v=XtDk7yc4VV8"

driver = webdriver.Chrome()
driver.maximize_window()


def good_soup(driver):
    driver.get(GOOD_SOUP)
    time.sleep(4)

    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()

    time.sleep(7)

    driver.close()
    print("\n\nGood soup.")


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