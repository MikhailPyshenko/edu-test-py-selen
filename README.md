# **Шаблон автоматизированного тестирования** 
* Учебный проект (и шаблон) автоматизации труда ручного тестирования.
* Основной функционал - UI скрипты на `python` с использованием библиотеки `selenium`.
* В качестве примера автоматизируется проект [saucedemo](https://www.saucedemo.com/v1/)
 
## Подготовка:

<details><summary>==[НАЖМИ]== Ссылки на скачивание и инструкции по настройке среды разработки</summary><p>

* [Скачать `Python` версии 13+](https://www.python.org/downloads/)
  * [Инструкция установки `Python` глава 2.1, эксплуатация глава 3](https://disk.yandex.ru/edit/d/ziggIjO2lsG0H2023WbIniPegnqahzm72s0qoIz-cKg6UlFmWEZta1prdw)
* [Скачать `git` версии 2.49+](https://git-scm.com/downloads)
  * [Инструкция установки и эксплуатации `git` глава 4.5](https://disk.yandex.ru/i/p6A-v9AiGy5qxA)
* IDE:
  * `OpenIDE` - Российский IDE
    * [Скачать версии 243+](https://openide.ru/download/)
  * `PyCharm` - Рекомендуемый способ взаимодействия с `python`
    * [Скачать версии Community Edition 2024+](https://www.jetbrains.com/ru-ru/pycharm/download/other.html)
    * [Установка глава 2.2 | Эксплуатация глава 4](https://disk.yandex.ru/edit/d/ziggIjO2lsG0H2023WbIniPegnqahzm72s0qoIz-cKg6UlFmWEZta1prdw)
  * `VSCode` - Популярный IDE
    * [Скачать версии 1.99+](https://code.visualstudio.com/docs/?dv=win64user)
</p></details>
* Подробнее в файлах `IDE.md` и `GIT.md`, в папке `docs`, в корневой директории проекта

## **Требования к запуску**
* Описаны в файле `requirements.txt`
* Установка требований из этого файла:
```
pip install -r requirements.txt
```
* Альтернативная установка требований:
```
pip install selenium webdriver_manager pytest pytest-html allure-pytest requests locust
```

## **Запуск авто-тестов**
### Pytest
* Запуск содержимого директории вида тестов.
* Виды: `smoke`, `accept`, `api` и `load`, например:
```
pytest test/smoke
```
* Запуск по маркерам `pytest`'а (фикстура `pytest.mark` и файл `pytest.ini`).
* Маркеры: `smoke`, `accept`, `core` и `test`, например:
```
pytest -m "smoke"
```
* Прочие команды `pytest`:
```
pytest --browser firefox                        # выбор браузера (chromium, webkit) (если описаны в pytest.ini)
pytest --headless true                          # скрыть браузер (если описаны в pytest.ini)
pytest -k "name"                                # пуск тестов по имени
pytest -n 4                                     # пуск тестов паралельно (потоки процессора)
pytest --alluredir=reports/allure-results       # пуск тестов с отчетом

Полная команда может выглядеть так:
pytest test/smoke --browser firefox --headless true --alluredir=reports/allure-results
```

## **Покрытые авто-тестами модули**
* **Авторизация**   page/login/login_page.py
* **Товары**        page/inventory/inventory_page.py
* **Корзина**       page/cart/cart_page.py
* **Покупка**       page/pay/pay_page.py

## **Архитектура проекта**
<details><summary>Структура директорий</summary><p>

```
/test-projectname/                  # корневой каталог (репозиторий) проекта авто-тестов
├── /page/                          # page object модели
│   ├── /login/                     # папка с page object моделью и данными модуля ЛОГИН
│   │   ├── login_page.py           # page object класс модуля ЛОГИН
│   │   ├── login_data.py           # тестовые данные модуля ЛОГИН
│   │   ├── login_locators.py       # селекторы элементов модулей ЛОГИН
│   │   └── __init__.py
│   ├── /inventory/                 # папка с page object моделью и данными модуля ТОВАРЫ
│   │   ├── inventory_page.py       # page object класс модуля ТОВАРЫ
│   │   ├── inventory_data.py       # тестовые данные модуля ТОВАРЫ
│   │   ├── inventory_locators.py   # селекторы элементов модулей ТОВАРЫ
│   │   └── __init__.py
│   ├── /cart/                      # папка с page object моделью и данными модуля КОРЗИНА
│   │   ├── cart_page.py            # page object класс модуля КОРЗИНА
│   │   ├── cart_data.py            # тестовые данные модуля КОРЗИНА
│   │   ├── cart_locators.py        # селекторы элементов модулей КОРЗИНА
│   │   └── __init__.py
│   ├── /pay/                       # папка с page object моделью и данными модуля ПОКУПКИ
│   │   ├── pay_page.py             # page object класс модуля ПОКУПКИ
│   │   ├── pay_locators.py         # селекторы элементов модулей ПОКУПКИ
│   │   ├── pay_data.py             # тестовые данные модуля ПОКУПКИ
│   │   └── __init__.py
│   ├── base_page.py                # базовый page object класс (основные методы работы со страницей)
│   └── __init__.py 
├── /test/                          # тестовые сценарии с группировкой по видам
│   ├── /smoke/                     # дымы (фронт)
│   │   ├── test_smoke_login.py
│   │   ├── test_smoke_inv.py
│   │   ├── test_smoke_cart.py
│   │   └── test_smoke_pay.py
│   ├── /accept/                    # приемка (фронт)
│   │   ├── test_accept_login.py
│   │   ├── test_accept_inv.py
│   │   ├── test_accept_cart.py
│   │   └── test_accept_pay.py
│   ├── /api/                       # апи (бэк)
│   │   └── test_api_login.py
│   ├── /load/                      # нагрузочное (locust)
│   │   └── test_locust.py
│   ├── test_run.py                 # запуск всех тестов
│   └── __init__.py
├── /config/                        # конфигурации
│   ├── conftest.py                 # фикстуры pytest
│   ├── logger.py                   # конфигурация логирования
│   └── __init__.py
├── /utils/                         # вспомогательные инструменты
│   ├── /drivers/                   # веб-драйвера и портативные браузеры
│   ├── actions.py                  # сложные методы и действия на страницах
│   ├── asserts.py                  # проверки
│   ├── helpers.py                  # вспомогательные элементы
│   └── __init__.py
├── /report/                        # отчеты и артефакты (если не подключено хранение в jenkins)
│   ├── /screenshots/               # скриншоты
│   ├── /allure-results/            # allure отчеты
│   ├── /pytest-html/               # pytest отчеты
│   ├── /locust/                    # locust отчеты нагрузочного
│   └── /logs/                      # логи выполнения тестов
├── /docs/                          # документация
│   ├── PLAN.md                     # документация проекта, план автоматизации, тест-кейсы и история изменений
│   ├── CODE.md                     # описание стиля кода в проекте
│   ├── ARCH.md                     # описание вариантов архитектур проекта
│   ├── MD.md                       # описание markdown разметки
│   ├── IDE.md                      # описание работы в различных IDE и их настройки
│   ├── TERMINAL.md                 # описание работы в различных терминалах (cmd\unix\bash)
│   └── GIT.md                      # описание работы с git и bitbucket
├── pytest.ini                      # конфигурация тестов
├── requirements.txt                # зависимости
├── README.md                       # описание проекта
└── .gitignore                      # игнор лист git
```
</p></details>

* Отчеты и артефакты папки `report` только для локального хранения, в эксплуатации подразумевается хранение артефактов в `jenkins`.
* Подробнее описано в файле `ARCH.md` в папке `docs` в корневой директории проекта

## **Работа в репозитории**
* **Пример безопасного workflow в `git`**
```
# Перед началом работы
git pull origin main

# После нужных изменений и ревью сформируйте инlекс
git add .

# Проверить, что нет лишних файлов
git status

# Создание коммита
git commit -m "Комментарий"

# Отправка изменений на сервер (-u чтобы запомнил ветки, потом можно просто git push)
git push -u origin main
```
#### **Подключение к репозиторию через `git`**:
* Подробнее описано в файле `GIT.md` в папке `docs` в корневой директории проекта