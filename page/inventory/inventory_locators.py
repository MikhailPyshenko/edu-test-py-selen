from selenium.webdriver.common.by import By

SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
ADD_TO_CART_1 = (By.ID, "add-to-cart-sauce-labs-backpack")
ADD_TO_CART_2 = (By.ID, "add-to-cart-sauce-labs-bike-light") 
REMOVE_FROM_CART_1 = (By.ID, "remove-sauce-labs-backpack")
REMOVE_FROM_CART_2 = (By.ID, "remove-sauce-labs-bike-light")
SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
INVENTORY_LIST = (By.CSS_SELECTOR, "#inventory_container > div")