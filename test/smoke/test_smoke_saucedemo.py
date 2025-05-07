import pytest
from selenium import webdriver
from page.login.login_page import LoginPage
from page.login.login_data import *
from page.inventory.inventory_page import InventoryPage
from page.inventory.inventory_data import *
from page.cart.cart_page import CartPage
from page.cart.cart_data import *
from page.pay.pay_page import PayPage
from page.pay.pay_data import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Или другой браузер
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)

@pytest.fixture
def pay_page(driver):
    return PayPage(driver)

@pytest.fixture
def logged_in_page(login_page):
    login_page.login()
    yield login_page.driver
    login_page.logout()

class TestSauceDemo:
    @pytest.mark.smoke
    def test_login_logout(self, login_page):
        """Проверка входа и выхода"""
        login_page.login()
        assert login_page.driver.current_url == INVENTORY_URL
        login_page.logout()
        assert login_page.driver.current_url == LOGIN_URL

    @pytest.mark.smoke
    def test_product_sorting(self, logged_in_page, inventory_page):
        """Проверка сортировки товаров"""
        inventory_page.sort_products_low_to_high()
        # Здесь можно добавить проверку сортировки

    @pytest.mark.smoke
    def test_add_to_cart(self, logged_in_page, inventory_page):
        """Добавление товаров в корзину"""
        inventory_page.add_products()
        inventory_page.cart_badge_value(2)
        inventory_page.remove_products()
        inventory_page.cart_badge_not_visible()

    @pytest.mark.smoke
    def test_cart(self, logged_in_page, cart_page, inventory_page):
        """Добавление товаров в корзину"""
        inventory_page.add_products()
        inventory_page.go_to_cart()
        # Проверка содержимого корзины

        cart_page.remove_products_from_cart()
        # Проверка очистки корзины

    @pytest.mark.smoke
    def test_checkout_flow(self, logged_in_page, inventory_page, cart_page, pay_page):
        """Оформление заказа"""
        inventory_page.add_products()
        inventory_page.go_to_cart()
        cart_page.checkout_go_to_pay()
        pay_page.fill_checkout_info()
        pay_page.finish_checkout()
        assert "complete" in pay_page.driver.current_url

    @pytest.mark.smokefull
    def test_full_flow(self, login_page, inventory_page, cart_page, pay_page):
        """Полный smoke-тест основного потока"""
        login_page.login()
        inventory_page.sort_products_low_to_high()
        inventory_page.add_products()
        inventory_page.go_to_cart()
        cart_page.checkout_go_to_pay()
        pay_page.fill_checkout_info()
        pay_page.finish_checkout()
        assert pay_page.driver.current_url == PAY_URL
        login_page.logout()
        assert login_page.driver.current_url == LOGIN_URL
