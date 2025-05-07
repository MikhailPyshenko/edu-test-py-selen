# Selenium для Python
* Инструкция по использованию фреймворка `selenium` в `python` для автоматизации UI тестирования.
---

## Основные особенности
* Selenium - это популярный фреймворк для автоматизации браузеров. Основные особенности:
  * Поддержка всех основных браузеров (Chrome, Firefox, Safari, Edge и др.)
  * Кроссплатформенность (Windows, macOS, Linux)
  * Поддержка множества языков программирования
  * Широкая экосистема инструментов и библиотек
  * Поддержка мобильного тестирования через Appium
  * Возможность интеграции с облачными сервисами (Sauce Labs, BrowserStack)
---

## Установка и настройка
* Установка `selenium`
```bash
pip install selenium
```
---
* Установка WebDriver для различных браузеров
```bash
# Chrome
https://sites.google.com/chromium.org/driver/
# Firefox
https://github.com/mozilla/geckodriver/releases
# Edge
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Safari (уже предустановлен на macOS)
```
---
* Дополнительные опции установки:
```bash
# Установка через менеджер WebDriver
pip install webdriver-manager
```
---

## Структура и расположение файлов
* WebDriver обычно располагается:
  * В PATH системы
  * В директории проекта
  * Указывается явно в коде
  * Тесты рекомендуется хранить в директории tests/
  * Конфигурационные файлы pytest обычно хранятся в pytest.ini или conftest.py
---

# Фикстуры и начальная настройка
## Базовые фикстуры в `conftest.py`
* Фикстура `browser`
```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
```
* Назначение:
  * Инициализация и управление экземпляром браузера.
* Что делает:
  * Создает экземпляр WebDriver с настройками
  * yield driver возвращает объект для использования в тестах
  * driver.quit() закрывает браузер после тестов
* Важно:
  * scope="session" означает один экземпляр на все тесты. Для изоляции используйте scope="function".
---
* Фикстура с выбором браузера
```python
@pytest.fixture(params=["chrome", "firefox"], scope="session")
def browser(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
```
---
* Фикстура с WebDriver Manager
```python
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()
```
---
* Итоговый пример файла `conftest.py`
```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(
        ChromeDriverManager().install(),
        options=options
    )
    
    driver.implicitly_wait(10)  # Неявные ожидания
    yield driver
    driver.quit()
```
---

# Параметризация
* Параметризация браузеров
```python
@pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
def test_multiple_browsers(browser_name: str, request):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    # тест
    driver.quit()
```
---
* Параметризация тестовых данных
```python
@pytest.mark.parametrize("username,password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
])
def test_login(browser, username: str, password: str):
    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login").click()
```
---

# Основные классы и методы
* Класс WebDriver
```python
# Навигация
driver.get("https://example.com")
driver.back()
driver.forward()
driver.refresh()

# Управление окнами
driver.maximize_window()
driver.minimize_window()
driver.set_window_size(1024, 768)

# Куки
driver.add_cookie({"name": "test", "value": "123"})
cookies = driver.get_cookies()
driver.delete_all_cookies()

# Скриншоты
driver.save_screenshot("screenshot.png")

# JavaScript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```
---
* Класс WebElement (поиск)
```python
from selenium.webdriver.common.by import By

# Локаторы
element = driver.find_element(By.ID, "username")
elements = driver.find_elements(By.CLASS_NAME, "item")

# Действия с элементами
element.click()
element.send_keys("text")
element.clear()
text = element.text
attribute = element.get_attribute("href")
is_displayed = element.is_displayed()
is_enabled = element.is_enabled()
is_selected = element.is_selected()
```
---
* Класс ActionChains (сложные действия)
```python
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
actions.move_to_element(menu).click(submenu).perform()
actions.drag_and_drop(source, target).perform()
actions.context_click(element).perform()
actions.double_click(element).perform()
```
---
* Класс Browser
```python
browser = playwright.chromium.launch(headless=False, slow_mo=50)
browser.close()
```
---
* Класс WebDriverWait (ожидания)
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "username")))
wait.until(EC.title_is("Expected Title"))
wait.until(EC.url_contains("login"))
wait.until(EC.element_to_be_clickable((By.ID, "submit")))
wait.until(EC.visibility_of_element_located((By.ID, "message")))
```
---
* Класс Select (работа с выпадающими списками)
```python
from selenium.webdriver.support.ui import Select

select = Select(driver.find_element(By.ID, "country"))
select.select_by_visible_text("Russia")
select.select_by_value("ru")
select.select_by_index(1)
options = select.options
first_selected = select.first_selected_option
```
---
* Алерты
```python
alert = driver.switch_to.alert
alert.accept()
alert.dismiss()
alert.send_keys("text")
text = alert.text
```
---
* Фреймы и окна
```python
# Переключение на фрейм
driver.switch_to.frame("frame_name")
driver.switch_to.frame(0)  # по индексу
driver.switch_to.default_content()

# Переключение на окно
main_window = driver.current_window_handle
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
```
---
* Пример теста с Selenium
```python
def test_login(browser):
    browser.get("https://example.com/login")
    
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    submit = browser.find_element(By.ID, "submit")
    
    username.send_keys("testuser")
    password.send_keys("password123")
    submit.click()
    
    welcome = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "welcome"))
    )
    
    assert "Welcome" in welcome.text
```
---