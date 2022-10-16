import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

from configs.config import Config

manager = ChromeDriverManager()
path = manager.install()


# Передача аргументов через переменные окружения не реализована
def pytest_addoption(parser):
    parser.addoption(
        "--base_host", action="store", help="Базовый host", default="www.timeapi.io",
    )


def pytest_configure(config):
    Config.configure(
        base_host=config.getoption('--base_host'),
    )


@pytest.fixture()
def browser():
    driver = Chrome(executable_path=path)
    driver.maximize_window()

    yield driver

    driver.quit()
