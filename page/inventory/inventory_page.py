from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage
from page.inventory.inventory_locators import *
from page.inventory.inventory_data import *

class InventoryPage(BasePage):
    def sort_products_low_to_high(self):
        self.select_option(SORT_DROPDOWN, SORT_OPTION_VALUE)

    def add_products(self):
        self.click(ADD_TO_CART_1)
        self.click(ADD_TO_CART_2)

    def remove_products(self):
        self.click(REMOVE_FROM_CART_1)
        self.click(REMOVE_FROM_CART_2)

    @property
    def cart_badge(self):
        return self.driver.find_element(By.CSS_SELECTOR, SHOPPING_CART_BADGE)

    def cart_badge_value(self, value):
        assert self.cart_badge.text == str(value), \
            f"Expected badge value {value}, got {self.cart_badge.text}"

    def cart_badge_not_visible(self):
        assert len(self.driver.find_elements(By.CSS_SELECTOR, SHOPPING_CART_BADGE)) == 0, \
            "Shopping cart badge is visible but shouldn't be"

    def go_to_cart(self):
        self.click(SHOPPING_CART)