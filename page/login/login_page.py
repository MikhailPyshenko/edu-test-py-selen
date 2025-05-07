from page.base_page import BasePage
from page.login.login_locators import *
from page.login.login_data import *

class LoginPage(BasePage):
    def login(self, username=STANDARD_USER, password=PASSWORD):
        self.navigate(LOGIN_URL)
        self.fill(USERNAME_INPUT, username)
        self.fill(PASSWORD_INPUT, password)
        self.click(LOGIN_BUTTON)
        self.wait_for_url(f"{LOGIN_URL}inventory.html")

    def login_error(self, username=ERROR_USER, password=PASSWORD):
        self.navigate(LOGIN_URL)
        self.fill(USERNAME_INPUT, username)
        self.fill(PASSWORD_INPUT, password)
        self.click(LOGIN_BUTTON)
        self.wait_for_url(f"{LOGIN_URL}inventory.html")

    def logout(self):
        self.click(MENU_BUTTON)
        self.click(LOGOUT_BUTTON)
        self.wait_for_url(LOGIN_URL)