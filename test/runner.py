import subprocess
import os

# Путь к директории с результатами Allure
allure_results_dir = "reports/allure-results"

# Удалить старые результаты, если нужно
if os.path.exists(allure_results_dir):
    for file in os.listdir(allure_results_dir):
        os.remove(os.path.join(allure_results_dir, file))
else:
    os.makedirs(allure_results_dir)

# Команда запуска pytest
command = [
    "pytest",
    "smoke/test_smoke_saucedemo.py",
    "--browser=firefox",
    "--headless",
]

# Запуск тестов
result = subprocess.run(command)

# Код завершения
exit(result.returncode)

#    "--alluredir=" + allure_results_dir,