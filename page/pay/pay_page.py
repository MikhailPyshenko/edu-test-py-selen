import allure
from selenium.webdriver.remote.webdriver import WebDriver
from page.base_page import BasePage
from config.utils.actions import ActionPage
from config.utils.asserts import AssertPage
from config.utils.reporter import ReportPage
from page.pay.pay_data import FIRST_NAME, LAST_NAME, ZIP_CODE
from page.pay.pay_locators import (
    FIRST_NAME_INPUT,
    LAST_NAME_INPUT,
    POSTAL_CODE_INPUT,
    CONTINUE_BUTTON,
    FINISH_BUTTON)


class PayPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.actions = ActionPage(driver)
        self.asserts = AssertPage(driver)
        self.report = ReportPage(driver)

    @allure.step("Заполнение данных для оплаты")
    def fill_checkout_info(self):
        """Заполняет информацию для оформления заказа"""
        self.actions.fill(FIRST_NAME_INPUT, FIRST_NAME)
        self.actions.fill(LAST_NAME_INPUT, LAST_NAME)
        self.actions.fill(POSTAL_CODE_INPUT, ZIP_CODE)
        self.actions.click(CONTINUE_BUTTON)
        self.report.attach_screenshot("После заполнения данных")

    @allure.step("Подтверждение покупки")
    def finish_checkout(self):
        """Завершает процесс оформления заказа"""
        self.actions.click(FINISH_BUTTON)
        self.report.attach_screenshot("После подтверждения покупки")