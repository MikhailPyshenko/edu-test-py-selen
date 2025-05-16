from config.utils.mock_generator import MockGenerator

PAY_URL = "https://www.saucedemo.com/checkout-complete.html"
# FIRST_NAME = "Mike"
# LAST_NAME = "Wazowski"
# ZIP_CODE = "2319"

USER = MockGenerator.user()
FIRST_NAME = USER["first_name"]
LAST_NAME = USER["last_name"]

ADDRESS = MockGenerator.address()
ZIP_CODE = ADDRESS["zip_code"]


def test_example():
    print(FIRST_NAME)  # Будет разным при каждом запуске (или фиксированным)
    print(LAST_NAME)
    print(ZIP_CODE)
