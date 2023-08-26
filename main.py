# Python program to demonstrate selenium

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get("https://www.youtube.com/")

print(driver.title)

time.sleep(10)

shorts_tab = driver.find_element(
    "xpath", "/html/body/ytd-app/div[1]/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[2]/a/yt-icon/yt-icon-shape/icon-shape/div")
shorts_tab.click()

time.sleep(20)

while True:
    shorts_screen = driver.find_element(
        "xpath", '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[4]/div[2]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div')
    shorts_screen.click()
    time.sleep(30)


driver.quit()
