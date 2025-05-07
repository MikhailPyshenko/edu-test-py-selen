# конфиг файл запуска браузера Selenium
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Конфигурация через pytest (CLI или pytest.ini)
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox",
                     choices=["chrome", "firefox", "edge"], help="Выбор браузера")
    parser.addoption("--headless", action="store_true", help="Пуск браузера в скрытом режиме")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,720")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1280")
        options.add_argument("--height=720")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    elif browser_name == "edge":
        from selenium.webdriver.edge.options import Options as EdgeOptions
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,720")
        driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=options)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def page(browser):
    yield browser