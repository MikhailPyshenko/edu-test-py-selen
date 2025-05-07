import time
from page.base_page import BasePage
from page.cart.cart_locators import *
from page.cart.cart_data import *


class CartPage(BasePage):
    def remove_products_from_cart(self):
        # Находим все кнопки удаления товаров
        remove_buttons = self.find_elements(REMOVE_BUTTONS)

        # Перебираем все кнопки и кликаем по каждой
        for btn in remove_buttons:
            btn.click()
            # Добавить паузу, если необходимо, чтобы дать время на обновление корзины
            time.sleep(1)  # Можно настроить паузу или заменить на явное ожидание