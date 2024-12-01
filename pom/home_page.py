from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://uitestingplayground.com/home"

    def navigate(self):
        self.driver.get(self.url)

    def is_element_present(self, locator):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, locator).is_displayed()
        except:
            return False
