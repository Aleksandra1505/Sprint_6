import allure

from locators.main_page_locators import MainPageLocators
from page_objects.BasePage import BasePageMetod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.header_locators import HeaderLocators


class MainPageMetod(BasePageMetod):
   @allure.step('Клик по вопросу')
   def click_to_question(self, num):
       self.scroll_to_element(MainPageLocators.last_question_locator)
       question = self.format_locators(MainPageLocators.question_locator, num)
       self.click_to_element(question)


   @allure.step('Отображение ответа на вопрос')
   def get_answer_for_question(self, num):
       answer_locator = (By.XPATH, f'//div[@id="accordion__panel-{num}"]/p')
       self.wait_for_element_to_be_visible(answer_locator)
       return self.get_text_from_element(answer_locator)

   def wait_for_element_to_be_visible(self, locator, timeout=10):
       WebDriverWait(self.driver, timeout).until(
           EC.visibility_of_element_located(locator)
       )

   def get_answer_for_question(self, num):
       answer_locator = (By.XPATH, f'//div[@id="accordion__panel-{num}"]/p')
       self.wait_for_element_to_be_visible(answer_locator)
       text = self.get_text_from_element(answer_locator)
       assert text != "", f"Ответ на вопрос {num} пустой!"
       return text

   @allure.step('Нажать на кнопку "Заказать"')
   def click_order_button(self, locator=HeaderLocators.button_header_order):
       self.scroll_to_element(locator)
       self.click_to_element(locator)

   @allure.step('Принять куки, если отображается плашка')
   def accept_cookie(self):
       try:
           self.wait_for_element(MainPageLocators.cookie_locator)
           self.click_to_element(MainPageLocators.cookie_locator)
       except Exception:
           pass  #если куки не отображаются, просто продолжаем
