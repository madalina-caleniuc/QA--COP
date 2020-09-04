from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FirstAss(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/madalina.caleniuc/Desktop/chromedriver_2")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)

    def test_first(self):
        driver = self.driver
        driver.get("https://www.google.com/")

        SEARCH_INPUT = "gLFyf"
        SEARCH_BY = "selenium python"
        GOOGLE_LOGO = "hplogo"
        INITIAL_LINK = "https://selenium-python.readthedocs.io/"

        self.wait.until(EC.visibility_of_element_located((By.ID, GOOGLE_LOGO)))
        searchInput = driver.find_element(By.CLASS_NAME, SEARCH_INPUT)
        searchInput.clear()
        searchInput.send_keys(SEARCH_BY)
        searchInput.send_keys(Keys.RETURN)

        firstElementFromList = driver.find_element_by_css_selector(".r>a")
        attribute_of_the_first_element = firstElementFromList.get_attribute('href')
        assert (INITIAL_LINK == attribute_of_the_first_element), "They don't match"

        firstElementFromList.click()
        headerLink = driver.find_element_by_class_name("headerlink")
        header_link_attribute = headerLink.get_attribute("href")
        new_attribute = attribute_of_the_first_element + "#selenium-with-python"
        self.assertEqual(header_link_attribute, new_attribute, "The header links don't match")

    def test_quick_search(self):
        driver = self.driver
        driver.get("https://selenium-python.readthedocs.io")
        self.wait = WebDriverWait(self.driver, 10)
        search_elem = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "q")))
        search_elem.send_keys("locating elements")
        search_elem.send_keys(Keys.RETURN)

        list_of_results = self.driver.find_elements_by_css_selector("a>span")
        first_strings = list_of_results[0].get_attribute("class")
        second_strings = list_of_results[1].get_attribute("class")

        first_elem_strings = list_of_results[0].text
        second_elem_strings = list_of_results[1].text
        final_result = first_elem_strings + " " + second_elem_strings

        assert (first_strings == "highlighted"), "The first element is not highlighted"
        assert (second_strings == "highlighted"), "The second element is not highlighted"
        assert (final_result == "Locating Elements"), "The search text is not OK"

    def test_find_alert(self):
        driver = self.driver
        driver.get("https://selenium-python.readthedocs.io")
        self.wait = WebDriverWait(self.driver, 10)
        api_elem = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "7. WebDriver API")))
        api_elem.click()
        alert_elem = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "7.3. Alerts")))
        alert_elem.click()
        module_elem = self.wait.until(
            EC.visibility_of_element_located((By.ID, "module-selenium.webdriver.common.alert")))
        module_elem_is_displayed = module_elem.is_displayed()

        assert (module_elem_is_displayed == True), "The Check Alerts section of the page is not visible"

    def test_scroll_down(self):
        driver = self.driver
        driver.get("https://selenium-python.readthedocs.io")
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        button_elem = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sphinx 1.8.5")))
        button_elem_is_displayed = button_elem.is_displayed()

        assert (button_elem_is_displayed == True), "No scroll down"

    def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()
