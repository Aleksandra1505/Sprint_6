import allure
import pytest
from tests.conftest import driver
from locators.main_page_locators import MainPageLocators
from page_objects.MainPage import MainPageMetod


class TestMainPage:
    @allure.title('Отображение ответа на вопрос')
    @allure.description("При тапе на вопрос открывается соответствующий по номеру ответ")
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
            (1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
            (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
            (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
            (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
            (5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
            (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
            (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPageMetod(driver)
        main_page_url = 'https://qa-scooter.praktikum-services.ru/'
        driver.get(main_page_url)
        main_page.accept_cookie()
        main_page.scroll_to_element(MainPageLocators.last_question_locator)
        main_page.click_to_question(num)
        assert main_page.get_answer_for_question(num) == result