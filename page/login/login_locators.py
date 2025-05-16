from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.ID, "user-name")
PASSWORD_INPUT = (By.ID, "password") 
LOGIN_BUTTON = (By.ID, "login-button")
MENU_BUTTON = (By.ID, "react-burger-menu-btn")
LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
ERROR_MESSAGE_BUTTON = (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")