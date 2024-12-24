from selenium.webdriver.common.by import By

class OrderPageLocators:
    order_header_locator = By.XPATH, '//*[@class="Order_Header__BZXOb"]' #заголовок страницы
    name_locator = By.XPATH, '//input[@placeholder="* Имя"]'
    surname_locator = By.XPATH, '//input[@placeholder="* Фамилия"]'
    address_locator = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    metro_button_locator = By.XPATH, "//input[@placeholder='* Станция метро']"
    metro_station_locator = By.XPATH, '//div[@class="select-search__select"]/ul/li[@data-index="{}"]'
    phone_number_locator = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    next_button_locator = By.XPATH, '//button[text()="Далее"]'

    date_locator = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    accept_date_locator = By.XPATH, '//div[@class="Order_Header__BZXOb" and text()="Про аренду"]'
    rent_time_locator = By.XPATH, '//div[@class="Dropdown-root"]'
    rent_to_one_day_locator = By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]'
    rent_to_two_days_locator = By.XPATH, '//div[@class="Dropdown-option" and text()="двое суток"]'
    black_checkbox_locator = By.XPATH, '//input[@id="black"]'
    grey_checkbox_locator = By.XPATH, '//input[@id="grey"]'
    comment_locator = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    order_button_locator = By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'

    button_yes_locator = By.XPATH, '//button[text()="Да"]'
    check_order_button_locator = By.XPATH, '//button[text()="Посмотреть статус"]'




