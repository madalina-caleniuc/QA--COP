# Assessment 2 - Part 1


from selenium import webdriver
import time

class LoginTest():

    def set_up_driver(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def login_validation(self):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(10)
        self.driver.find_element_by_link_text("Welcome Admin").click()
        self.driver.find_element_by_link_text("Logout").click()
        
    def close_browser(self):
        self.driver.close()
        self.driver.quit()

        
login1 = LoginTest()
login1.set_up_driver()
login1.login_validation()
login1.close_browser()
