from page.base_page import BasePage
from page.pay.pay_data import *
from page.pay.pay_locators import *

class PayPage(BasePage):
    def fill_checkout_info(self):
        self.fill(FIRST_NAME_INPUT, FIRST_NAME)
        self.fill(LAST_NAME_INPUT, LAST_NAME)
        self.fill(POSTAL_CODE_INPUT, ZIP_CODE)
        self.click(CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(FINISH_BUTTON)