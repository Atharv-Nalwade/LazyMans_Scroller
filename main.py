from decouple import config
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchWindowException
from googleapiclient.discovery import build
import isodate
import re
import time

api_key = config('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

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

            # Introduce a short delay to allow content to load
            time.sleep(2)
            start_time = time.time()
            short_url = re.search(r"shorts/(.+)$", driver.current_url).group(1)
            video_request = youtube.videos().list(
                part='contentDetails',
                id=short_url
            )
            response = video_request.execute()
            if 'items' in response:
                video_item = response['items'][0]
                content_details = video_item['contentDetails']
                duration = content_details['duration']

                # Parse the duration from ISO 8601 format
                duration_seconds = int(isodate.parse_duration(duration).total_seconds())
                print(f"{short_url} and its duration is {duration_seconds} seconds")
                end_time = time.time()
                print(f"Time taken to get duration: {end_time - start_time} seconds")
            
            time.sleep(duration_seconds-(end_time-start_time))  # Sleep for the current short's duration
            
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
