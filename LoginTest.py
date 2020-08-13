# Assessment 2 - Part 1

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FirstAss(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/madalina.caleniuc/Desktop/chromedriver_2")
        self.driver.get("https://www.google.com/search?")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)

    def test_search(self):
        input_elem = self.driver.find_element_by_name("q")
        input_elem.send_keys("selenium python")
        input_elem.send_keys(Keys.RETURN)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".r>a")))
        result = self.driver.find_element_by_css_selector(".r>a")
        link = result.get_attribute("href")
        assert link == "https://selenium-python.readthedocs.io/"
        result.click()
        assert self.driver.current_url == link

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
