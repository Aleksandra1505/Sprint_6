from selenium.webdriver.common.by import By

class MainPageLocators:
    question_locator = By.ID, 'accordion__heading-{}' # вопросы в разделе faq
    answer_locator = By.XPATH, '//div[@id="accordion__panel-{}"]/p' # ответы в разделе faq
    last_question_locator = By.ID, 'accordion__heading-7' # последний вопрос в разделе faq
    button_middle_order = By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']" # кнопка Заказать в блоке как это работает
    cookie_locator = By.ID, 'rcc-confirm-button'  # принять куки

