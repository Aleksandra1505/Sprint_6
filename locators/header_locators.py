from selenium.webdriver.common.by import By

class HeaderLocators:
    button_header_order = By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[contains(text(), 'Заказать')]"  # кнопка Заказать в хэддере
    logo_scooter_locator = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'  # лого самокат
    logo_yandex_locator = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'  # лого яндекс
    botton_find_locator = By.XPATH, '//button[text()="Найти"]' # кнопка Найти в хэддере
    text_locator = By.CLASS_NAME, 'Home_Header__iJKdX' # блок про самокат