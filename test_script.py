import unittest
from main import create_driver, is_driver_alive
import time
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
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
        # Replace with a URL you want to test
        self.driver.get("https://www.example.com")

    # Check if the new driver is alive after performing an action
        self.assertTrue(is_driver_alive(self.driver))

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
        # Replace 'YOUR_SHORT_URL_HERE' with the actual short URL you want to test
        short_url = 'https://www.youtube.com/shorts/rUJr4PLA91E'

        # Make an API call to get video details using the 'youtube' object
        video_request = youtube.videos().list(
            part='contentDetails',
            id=short_url
        )
        response = video_request.execute()

        # Check if the API call received a response
        self.assertTrue('items' in response, "API call did not return 'items'")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
