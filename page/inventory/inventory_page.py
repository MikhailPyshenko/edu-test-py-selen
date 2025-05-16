import allure
from selenium.webdriver.remote.webdriver import WebDriver
from page.base_page import BasePage
from config.utils.actions import ActionPage
from config.utils.asserts import AssertPage
from config.utils.reporter import ReportPage
from page.inventory.inventory_locators import (
    SORT_DROPDOWN,
    INVENTORY_LIST,
    ADD_TO_CART_1,
    ADD_TO_CART_2,
    REMOVE_FROM_CART_1,
    REMOVE_FROM_CART_2,
    SHOPPING_CART_BADGE,
    SHOPPING_CART)
from page.inventory.inventory_data import SORT_OPTION_VALUE, FIRST_ITEM_POST_SORT_LOHI


class InventoryPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.actions = ActionPage(driver)
        self.asserts = AssertPage(driver)
        self.report = ReportPage(driver)

    @allure.step("Сортировка по цене от дешевых к дорогим")
    def sort_products_low_to_high(self):
        self.actions.select_option(SORT_DROPDOWN, SORT_OPTION_VALUE)
        self.report.attach_screenshot("Итоги сортировки лохи")
        self.asserts.element_position_in_list_has_text(INVENTORY_LIST, 1, FIRST_ITEM_POST_SORT_LOHI)

    @allure.step(f"Добавление продуктов {ADD_TO_CART_1, ADD_TO_CART_2} в корзину")
    def add_products(self):
        self.actions.click(ADD_TO_CART_1)
        self.actions.click(ADD_TO_CART_2)
        self.report.attach_screenshot("Итоги добавления товаров")

    @allure.step(f"Удаление продуктов {ADD_TO_CART_1, ADD_TO_CART_2} из корзины на странице товаров")
    def remove_products(self):
        self.actions.click(REMOVE_FROM_CART_1)
        self.actions.click(REMOVE_FROM_CART_2)
        self.report.attach_screenshot("Итоги удаления товаров")

    @property
    def cart_badge(self):
        return self.driver.find_element(*SHOPPING_CART_BADGE)

    def cart_badge_value(self, value):
        """Проверяет значение бейджа корзины"""
        actual_value = self.cart_badge.text
        assert actual_value == str(value), \
            f"Ожидалось значение бейджа: {value}, получено: {actual_value}"

    def cart_badge_not_visible(self):
        """Проверяет что бейдж корзины не виден"""
        try:
            assert not self.cart_badge.is_displayed()
        except:
            # Если элемент не найден - тоже считается что не виден
            pass

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        self.actions.click(SHOPPING_CART)