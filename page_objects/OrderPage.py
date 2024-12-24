import allure

from locators.order_page_locators import OrderPageLocators
from page_objects.BasePage import BasePageMetod
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.helpers import generate_random_name, generate_random_last_name, generate_address, generate_telephone_number, generate_random_metro_station, generate_random_date

class OrderPageMetood(BasePageMetod):

    @allure.step('Ввести данные в элемент')
    def set_text_to_element(self, locator, text):
        element = self.find_elements_with_wait(locator)
        element.send_keys(text)

    @allure.step('Ввести номер в элемент')
    def set_number_to_locator(self, locator_num, num):
        method, locator = locator_num
        locator = locator.format(num)
        return method, locator

    @allure.step('Выбрать элемент из выпадающего списка')
    def select_element_from_menu(self, locator_menu, locator_item):
        self.click_to_element(locator_menu)
        self.scroll_to_element(locator_item)
        self.click_to_element(locator_item)

    @allure.step('Дождаться элемент на другой странице')
    def tab_switch(self, locator, time=10):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step('Сделать заказ')
    @allure.description('Заполнить поля данными и подтвердить создание заказа')
    def set_form_to_order(self, rent, checkbox, comment):
        #заполнить форму заказа №1
        self.set_text_to_element(OrderPageLocators.name_locator, generate_random_name())
        self.set_text_to_element(OrderPageLocators.surname_locator, generate_random_last_name())
        self.set_text_to_element(OrderPageLocators.address_locator, generate_address())
        # Кликнуть по полю метро
        self.click_to_element(OrderPageLocators.metro_button_locator)
        # Получаем случайную станцию и выбираем её в выпадающем списке
        metro_station = generate_random_metro_station()
        self.click_to_element(self.set_number_to_locator(OrderPageLocators.metro_station_locator, metro_station))

        self.set_text_to_element(OrderPageLocators.phone_number_locator, generate_telephone_number())
        self.click_to_element(OrderPageLocators.next_button_locator)

        #заполнить форму заказа №2
        self.set_text_to_element(OrderPageLocators.date_locator, generate_random_date())
        self.click_to_element(OrderPageLocators.accept_date_locator)
        self.select_element_from_menu(OrderPageLocators.rent_time_locator, rent)
        self.click_to_element(checkbox)
        self.set_text_to_element(OrderPageLocators.comment_locator, comment)
        self.find_elements_with_wait(OrderPageLocators.order_button_locator)
        self.click_to_element(OrderPageLocators.order_button_locator)

        #подтвердить заказ
        self.click_to_element(OrderPageLocators.button_yes_locator)










