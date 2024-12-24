import allure
from locators.order_page_locators import OrderPageLocators
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators


class TestOrderPage:
    @allure.title('Заказ самоката через кнопку "Заказать" в хедере')
    @allure.description("Тест проверяет успешное оформление заказа самоката через разные точки входа")

    def test_order_from_header(self, main_page, order_page):
        main_page_url = 'https://qa-scooter.praktikum-services.ru/'
        main_page.driver.get(main_page_url)
        main_page.accept_cookie()

        main_page.click_to_element(HeaderLocators.button_header_order)

        order_page.set_form_to_order(
            rent=OrderPageLocators.rent_to_one_day_locator,
            checkbox=OrderPageLocators.black_checkbox_locator,
            comment="Тестовый заказ через хедер"
        )

        assert order_page.is_element_visible(OrderPageLocators.check_order_button_locator), \
            "Попап с кнопкой 'Посмотреть статус' не появился, заказ не был успешно создан!"

    @allure.title('Заказ самоката через кнопку "Заказать" в футере')
    def test_order_from_futter(self, main_page, order_page):
        main_page_url = 'https://qa-scooter.praktikum-services.ru/'
        main_page.driver.get(main_page_url)
        main_page.accept_cookie()

        main_page.scroll_to_element(MainPageLocators.last_question_locator)
        main_page.click_to_element(MainPageLocators.button_middle_order)

        main_page.click_to_element(HeaderLocators.button_header_order)
        order_page.set_form_to_order(
            rent=OrderPageLocators.rent_to_one_day_locator,
            checkbox=OrderPageLocators.black_checkbox_locator,
            comment="Тестовый заказ через хедер"
        )

        assert order_page.is_element_visible(OrderPageLocators.check_order_button_locator), \
            "Попап с кнопкой 'Посмотреть статус' не появился, заказ не был успешно создан!"


