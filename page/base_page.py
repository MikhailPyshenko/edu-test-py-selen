from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, locator)
        )).click()

    def fill(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, locator)
        )).send_keys(text)

    def select_option(self, locator, value):
        select = Select(self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locator))
        ))
        select.select_by_value(value)

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, locator)
            ))
            return True
        except:
            return False

    def find_elements(self, locator):
        """Метод для поиска нескольких элементов по локатору"""
        return self.driver.find_elements(By.CSS_SELECTOR, locator)