import pytest
import allure
from page.login.login_page import LoginPage
from page.login.login_data import LOGIN_URL
from page.inventory.inventory_page import InventoryPage
from page.inventory.inventory_data import INVENTORY_URL
from page.cart.cart_page import CartPage
from page.cart.cart_data import *
from page.pay.pay_page import PayPage
from page.pay.pay_data import PAY_URL


@pytest.fixture
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture
def inventory_page(browser):
    return InventoryPage(browser)


@pytest.fixture
def cart_page(browser):
    return CartPage(browser)


@pytest.fixture
def pay_page(browser):
    return PayPage(browser)


@pytest.fixture
def login_in_page(login_page):
    login_page.login()
    yield login_page.driver
    login_page.logout()


# pytest test/smoke/test_smoke_saucedemo.py::TestSauceDemo --browser=firefox --headless --alluredir=reports/allure-results
@allure.epic("Приложение SauceDemo")
@allure.feature("Дымовые тесты")
class TestSauceDemo:

    # pytest test/smoke/test_smoke_saucedemo.py::TestSauceDemo::test_login_logout --browser=firefox --headless --alluredir=reports/allure-results
    @allure.title("Проверка входа и выхода")
    @allure.description("Проверяет, что пользователь может авторизоваться и выйти из системы")
    @allure.tag("smoke", "auth")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_logout(self, login_page):
        """Проверка входа и выхода"""
        login_page.login()
        with allure.step("Проверяем, что попали на страницу инвентаря"):
            login_page.asserts.url_is(INVENTORY_URL)
        login_page.logout()
        with allure.step("Проверяем, что вернулись на страницу логина"):
            login_page.asserts.url_is(LOGIN_URL)

    # pytest test/smoke/test_smoke_saucedemo.py::TestSauceDemo::test_login_locked --browser=firefox --headless --alluredir=reports/allure-results
    @allure.title("Проверка входа в заблокированного юзера")
    @allure.description("Проверяет, что заблокированный юзер не доступен к логину")
    @allure.tag("smoke", "ban")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_locked(self, login_page):
        """Проверка входа и выхода"""
        login_page.login_locked()
        with allure.step("Проверяем, что остались на странице логина"):
            login_page.asserts.url_is(LOGIN_URL)

    # pytest test/smoke/test_smoke_saucedemo.py::TestSauceDemo::test_product_sorting --browser=firefox --headless --alluredir=reports/allure-results
    @allure.title("Проверка сортировки товаров")
    @allure.description("Проверяет сортировку товаров по возрастанию цены")
    @allure.tag("smoke", "inventory")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_product_sorting(self, login_in_page, inventory_page):
        """Проверка сортировки товаров"""
        inventory_page.sort_products_low_to_high()

    # pytest test/smoke/test_smoke_saucedemo.py::TestSauceDemo::test_add_to_cart --browser=firefox --headless --alluredir=reports/allure-results
    @allure.title("Проверка добавления и удаления товаров из корзины")
    @allure.description("Проверяет, что товары добавляются и удаляются из корзины")
    @allure.tag("smoke", "cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_add_to_cart(self, login_in_page, inventory_page):
        """Добавление товаров в корзину"""
        inventory_page.add_products()
        inventory_page.cart_badge_value(2)
        inventory_page.remove_products()
        inventory_page.cart_badge_not_visible()

    # pytest test/smoke/test_smoke_saucedemo.py::TestSauceDemo::test_cart --browser=firefox --headless --alluredir=reports/allure-results
    @allure.title("Проверка содержимого и очистки корзины")
    @allure.description("Добавляет товары в корзину, переходит в неё и очищает")
    @allure.tag("smoke", "cart")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_cart(self, login_in_page, cart_page, inventory_page):
        """Добавление товаров в корзину"""
        inventory_page.add_products()
        inventory_page.go_to_cart()
        cart_page.products_in_cart(2)
        cart_page.remove_products_from_cart()
        cart_page.nothing_in_cart()

    # pytest test/smoke/test_smoke_saucedemo.py::TestSauceDemo::test_checkout_flow --browser=firefox --headless --alluredir=reports/allure-results
    @allure.title("Оформление заказа")
    @allure.description("Проходит полный путь оформления заказа с добавлением товара")
    @allure.tag("smoke", "checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_checkout_flow(self, login_in_page, inventory_page, cart_page, pay_page):
        """Оформление заказа"""
        inventory_page.add_products()
        inventory_page.cart_badge_value(2)
        inventory_page.go_to_cart()
        cart_page.products_in_cart(2)
        cart_page.checkout_go_to_pay()
        pay_page.fill_checkout_info()
        pay_page.finish_checkout()
        with allure.step("Проверка URL успешного завершения покупки"):
            assert "complete" in pay_page.driver.current_url
        cart_page.nothing_in_cart()

    # pytest test/smoke/test_smoke_saucedemo.py::TestSauceDemo::test_full_flow --browser=firefox --headless --alluredir=reports/allure-results
    @allure.title("Полный путь пользователя от логина до оформления")
    @allure.description("Smoke: от логина до финального экрана завершения покупки")
    @allure.tag("smokefull", "e2e")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smokefull
    def test_full_flow(self, login_page, inventory_page, cart_page, pay_page):
        """Полный smoke-тест основного потока"""
        login_page.login()
        inventory_page.sort_products_low_to_high()
        inventory_page.add_products()
        inventory_page.cart_badge_value(2)
        inventory_page.go_to_cart()
        cart_page.products_in_cart(2)
        cart_page.checkout_go_to_pay()
        pay_page.fill_checkout_info()
        pay_page.finish_checkout()
        login_page.asserts.url_is(PAY_URL)
        login_page.logout()
        login_page.asserts.url_is(LOGIN_URL)