from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePageMetod:
   def __init__(self, driver):
       self.driver = driver

   @allure.step('Найти элемент на странице и дождаться его загрузки')
   def find_elements_with_wait(self, locator, timeout=10):
       return WebDriverWait(self.driver, timeout).until(
           EC.presence_of_element_located(locator),
           message=f"Элемент с локатором {locator} не найден на странице"
       )

   @allure.step('Проверить видимость элемента на странице')
   def is_element_visible(self, locator, timeout=10):
       # находим элемент
       element = self.find_elements_with_wait(locator, timeout)
       # проверяем, что элемент видимый
       return element.is_displayed()

   @allure.step('Тап по элементу (с использованием JavaScript)')
   def click_to_element(self, locator, timeout=10):
       element = WebDriverWait(self.driver, timeout).until(
           EC.element_to_be_clickable(locator),
           message=f"Элемент с локатором {locator} не кликабелен"
       )
       try:
           element.click()  # пробуем кликнуть "обычным" методом
       except Exception:
           # если обычный клик не работает, используем JavaScript
           self.driver.execute_script("arguments[0].click();", element)

   @allure.step('Получить текст')
   def get_text_from_element(self, locator):
       element = self.find_elements_with_wait(locator)
       return element.text

   @allure.step('Получить элемент')
   def wait_for_element(self, locator):
       WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

   @allure.step('Скролл до элемента')
   def scroll_to_element(self, locator):
       element = self.driver.find_element(*locator)
       self.driver.execute_script('arguments[0].scrollIntoView();', element)

   @allure.step('')
   def format_locators(self, locator_1, num):
       method, locator = locator_1
       formatted_locator = locator.format(num)
       return (method, formatted_locator)
