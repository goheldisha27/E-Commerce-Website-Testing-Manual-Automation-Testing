import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"


class SauceDemoLoginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280, 900)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(BASE_URL)

    def test_valid_login_opens_inventory(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        self.wait.until(EC.url_contains("inventory.html"))
        self.assertIn("inventory.html", self.driver.current_url)

    def test_invalid_login_shows_error(self):
        self.driver.find_element(By.ID, "user-name").send_keys("wrong_user")
        self.driver.find_element(By.ID, "password").send_keys("wrong_password")
        self.driver.find_element(By.ID, "login-button").click()
        error = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        self.assertTrue(error.is_displayed())
        self.assertNotIn("inventory.html", self.driver.current_url)

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
