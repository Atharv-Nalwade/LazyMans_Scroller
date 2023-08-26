import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, NoSuchWindowException
import time
import keyboard  # Import the keyboard library


def create_driver():
    return webdriver.Firefox()


def is_driver_alive(driver):
    try:
        driver.title
        return True
    except (WebDriverException, NoSuchWindowException):
        return False


def main():
    driver = create_driver()
    driver.get("https://www.youtube.com/")

    print(driver.title)

    time.sleep(10)

    shorts_tab = driver.find_element(
        "xpath", "/html/body/ytd-app/div[1]/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[2]/a/yt-icon/yt-icon-shape/icon-shape/div")
    shorts_tab.click()

    time.sleep(20)

    try:
        while is_driver_alive(driver):
            shorts_screen = driver.find_element(
                "xpath", '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[4]/div[2]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div')
            shorts_screen.click()
            time.sleep(30)

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
