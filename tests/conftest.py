import pytest
from page_objects.MainPage import MainPageMetod
from page_objects.OrderPage import OrderPageMetood
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()

# Фикстура для страницы главной страницы
@pytest.fixture
def main_page(driver):
    return MainPageMetod(driver)

# Фикстура для страницы заказа
@pytest.fixture
def order_page(driver):
    return OrderPageMetood(driver)