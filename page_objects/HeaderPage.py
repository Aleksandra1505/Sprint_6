import allure

from locators.header_locators import HeaderLocators
from page_objects.BasePage import BasePageMetod
from selenium.webdriver.support.ui import WebDriverWait

class HeaderPageMetood(BasePageMetod):

    @allure.step('Нажать на логотип Яндекса')
    def go_to_yandex_logo(self):
        self.click_to_element(HeaderLocators.logo_yandex_locator)

    @allure.step('Нажать на логотип Самоката')
    def go_to_logo_scooter(self):
        self.click_to_element(HeaderLocators.logo_scooter_locator)

    @allure.step('Получить текст с главной страницы')
    def get_txt_from_main_page(self):
        text = self.get_text_from_element(HeaderLocators.text_locator)
        return text

    @allure.step('Получить текущий URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключиться на новое окно браузера')
    def switch_to_new_window(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1,
            message="Новое окно не открылось"
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
