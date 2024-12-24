import allure
from locators.header_locators import HeaderLocators
from page_objects.HeaderPage import HeaderPageMetood
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHeaderPage:
    @allure.title('Переход на главную страницу при клике на логотип "Самоката"')
    def test_logo_scooter_redirects_to_main_page(self, main_page):
        order_page_url = 'https://qa-scooter.praktikum-services.ru/order'
        main_page.driver.get(order_page_url)
        main_page.click_to_element(HeaderLocators.logo_scooter_locator)
        header_page = HeaderPageMetood(main_page.driver)

        main_page_url = 'https://qa-scooter.praktikum-services.ru/'
        assert header_page.get_current_url() == main_page_url, \
        "Клик на логотип Самоката не привел на главную страницу"

    @allure.title('Переход на главную страницу Дзена при клике на логотип "Самоката"')
    def test_logo_yandex_redirects_to_dzen(self, main_page):
        main_page_url = 'https://qa-scooter.praktikum-services.ru/'
        dzen_url = 'https://dzen.ru/?yredirect=true'

        main_page.driver.get(main_page_url)
        main_page.click_to_element(HeaderLocators.logo_yandex_locator)

        main_page.driver.switch_to.window(main_page.driver.window_handles[1])

        WebDriverWait(main_page.driver, 10).until(
            EC.url_contains(dzen_url)  # Ожидаем, что URL будет содержать часть URL Дзена
        )

        header_page = HeaderPageMetood(main_page.driver)

        assert header_page.get_current_url().startswith(dzen_url), \
            "Клик на логотип Яндекса не открыл главную страницу Дзена"
