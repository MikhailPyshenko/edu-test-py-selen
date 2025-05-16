import allure
from selenium.webdriver.remote.webdriver import WebDriver
from page.base_page import BasePage
from config.utils.actions import ActionPage
from config.utils.asserts import AssertPage
from config.utils.reporter import ReportPage
from page.cart.cart_locators import CHECKOUT_BUTTON, CART_LIST, CART_ITEM
from page.inventory.inventory_locators import REMOVE_FROM_CART_1, REMOVE_FROM_CART_2


class CartPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.actions = ActionPage(driver)
        self.asserts = AssertPage(driver)
        self.report = ReportPage(driver)

    @allure.step("Проверяем заполненность корзины")
    def products_in_cart(self, expected_count: int = None):
        self.report.attach_screenshot("Товары в корзине")
        self.asserts.element_is_visible(CART_LIST)
        # Проверка количества товаров
        if expected_count is not None:
            self.asserts.element_count_is(CART_ITEM, expected_count)
        # Проверка наличия товаров (первого элемента)
        items = self.driver.find_elements(*CART_ITEM)
        if items:
            self.asserts.element_is_visible(CART_ITEM)  # Проверяем первый элемент

    @allure.step("Проверяем пустоту корзины")
    def nothing_in_cart(self):
        self.report.attach_screenshot("Пустота в корзине")
        self.asserts.element_count_is(CART_ITEM, 0)
        self.asserts.element_is_hidden(CART_ITEM)

    @allure.step("Удаляем продукт из корзины")
    def remove_products_from_cart(self):
        self.actions.click(REMOVE_FROM_CART_1)
        self.actions.click(REMOVE_FROM_CART_2)

    @allure.step("Переход к покупке")
    def checkout_go_to_pay(self):
        self.actions.click(CHECKOUT_BUTTON)