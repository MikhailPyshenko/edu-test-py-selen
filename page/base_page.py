from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger import get_logger

HOME_URL = "https://www.saucedemo.com/"
BURGER_MENU = (By.ID, "react-burger-menu-btn")


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)  # 5 секунд по умолчанию
        self.logger = get_logger(self.__class__.__name__)

    def goto_home(self):
        """Переходит на домашнюю страницу"""
        self.logger.info(f"Переход на домашнюю страницу: {HOME_URL}")
        self.driver.get(HOME_URL)

    def burger_menu(self):
        """Кликает по кнопке бургер-меню"""
        self.logger.info("Клик по бургер-меню")
        element = self.wait.until(EC.element_to_be_clickable(BURGER_MENU))
        element.click()