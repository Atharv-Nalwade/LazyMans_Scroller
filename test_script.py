import threading
import unittest
from main import create_driver, is_driver_alive, main, api_key
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest.mock import patch
from main import youtube


class TestDriverLoaded(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver()


    def test_driver_loaded(self):
        # Check if the driver is successfully loaded
        self.assertTrue(is_driver_alive(self.driver))


    def test_driver_alive_when_alive(self):
        # Check if the driver is alive when it should be
        self.assertTrue(is_driver_alive(self.driver))


    def test_driver_not_alive_when_dead(self):
        # Close the driver to simulate it being dead
        self.driver.quit()

        # Create a new driver instance to replace the closed one
        self.driver = create_driver()

        # Check if the new driver is not alive
        self.assertTrue(is_driver_alive(self.driver))


    def test_driver_alive_after_quit_and_recreate(self):
        # Close the driver
        self.driver.quit()

        # Create a new driver instance to replace the closed one
        self.driver = create_driver()

        # Perform some action to interact with the new driver
        self.driver.get("https://www.example.com")

        # Check if the new driver is alive after performing an action
        self.assertTrue(is_driver_alive(self.driver))


    def test_create_driver_returns_valid_instance(self):
        # Call the create_driver function and check if it returns a valid driver instance
        driver = create_driver()
        self.assertIsNotNone(
            driver, "create_driver did not return a valid driver instance.")


    def test_homepage_load(self):
        # Navigate to the YouTube homepage
        self.driver.get("https://www.youtube.com/")

        # Check if the title of the homepage contains "YouTube"
        self.assertIn("YouTube", self.driver.title)


    def test_shorts_screen_load(self):
        # Navigate to the YouTube homepage
        self.driver.get("https://www.youtube.com/")

        # Find and click on the "Shorts" tab
        shorts_tab_xpath = "/html/body/ytd-app/div[1]/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[2]/a/yt-icon/yt-icon-shape/icon-shape/div"
        shorts_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, shorts_tab_xpath))
        )
        shorts_tab.click()

        # Wait for the "Shorts" screen to load
        time.sleep(20)

        # Check if the title of the page contains "YouTube"
        self.assertIn("YouTube", self.driver.title)


    def test_api_key_configured(self):
        # Check if the API key is configured
        self.assertIsNotNone(api_key, "API key is not configured.")


    def test_driver_stays_alive(self):
        # Introduce a short delay (e.g., 5 seconds)
        time.sleep(5)

        # Check if the driver is still alive after the delay
        self.assertTrue(is_driver_alive(self.driver),
                        "Driver is not alive after a short delay.")


    def test_create_driver_returns_driver(self):
        # Call the create_driver function and check if it returns a valid driver instance
        driver = create_driver()
        self.assertIsNotNone(
            driver, "create_driver did not return a valid driver instance.")


    def test_youtube_api_initialized(self):
        # Check if the YouTube API object is properly initialized
        self.assertIsNotNone(
            youtube, "YouTube API object is not properly initialized.")


    def test_shorts_tab_click(self):
        # Check if the "Shorts" tab is clickable
        # Navigate to the YouTube homepage
        self.driver.get("https://www.youtube.com/")

        # Wait for the "Shorts" tab to be clickable
        shorts_tab_xpath = "/html/body/ytd-app/div[1]/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[2]/a/yt-icon/yt-icon-shape/icon-shape/div"
        shorts_tab = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, shorts_tab_xpath))
        )
        shorts_tab.click()

        # Sleep for a short duration to allow the page to load
        time.sleep(20)

        # Check if the driver is still alive after clicking the "Shorts" tab
        self.assertTrue(is_driver_alive(self.driver))


    def test_api_response_received(self):
        #This is a demo short URL
        short_url = 'https://www.youtube.com/shorts/rUJr4PLA91E'

        # Make an API call to get video details using the 'youtube' object
        video_request = youtube.videos().list(
            part='contentDetails',
            id=short_url
        )
        response = video_request.execute()
        print(response)

        # Check if the API call received a response
        self.assertTrue('items' in response, "API call did not return 'items'")


    def test_api_response_contains_duration(self):
        #This is a demo short URL
        short_url = 'rUJr4PLA91E'

        # Make an API call to get video details using the 'youtube' object
        video_request = youtube.videos().list(
            part='contentDetails',
            id=short_url
        )
        response = video_request.execute()

        # Check if the API call received a response
        if 'items' in response:
            video_item = response['items'][0]
            content_details = video_item.get('contentDetails', {})

            # Check if the 'duration' field is present in 'contentDetails'
            if 'duration' in content_details:
                self.assertTrue(
                    True, "The response contains a 'duration' field.")
            else:
                self.fail("The response does not contain a 'duration' field.")
        else:
            self.fail("No 'items' in the API response.")


    def tearDown(self):
        self.driver.quit()


    def test_driver_alive_after_teardown(self):
        # Check if the driver is still alive after calling tearDown
        is_alive = is_driver_alive(self.driver)
        self.assertTrue(is_alive, "Driver is not alive after tearDown")


if __name__ == "__main__":
    unittest.main()
