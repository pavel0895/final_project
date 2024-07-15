import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.logger = browser.logger
        self.LINK_OPENCART = (By.LINK_TEXT, "Specials")
        self.SEARCH_FIELD = (By.XPATH, "//*[@id='search']")
        self.BUTTON_SEARCH = (By.CSS_SELECTOR, "button[type='button']")
        self.BUTTON_CART = (By.XPATH, "//*[@id='header-cart']/div/button")
        self.CURRENCY_FORM = (By.XPATH, "//*[@id='form-currency']/div/a/span")

    @property
    @allure.step("Находим ссылку")
    def get_link_opencart(self):
        try:
            self.logger.debug("Get link opencart")
            return self.get_element(self.LINK_OPENCART)
        except NoSuchElementException:
            self.logger.error("Link opencart not found")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            raise NoSuchElementException("Link opencart not found")

    @property
    @allure.step("Находим поле 'поиск'")
    def get_search_field(self):
        try:
            self.logger.debug("Get search field")
            return self.get_element(self.SEARCH_FIELD)
        except NoSuchElementException:
            self.logger.error("Search field not found")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            raise NoSuchElementException("Search field not found")

    @property
    @allure.step("Находим форму с отображением валют")
    def get_currency_form(self):
        try:
            self.logger.debug("Get currency form")
            return self.get_element(self.CURRENCY_FORM)
        except NoSuchElementException:
            self.logger.error("Currency form not found")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            raise NoSuchElementException("Currency form not found")

    @allure.step("Нажимаем на кнопку 'поиск'")
    def click_button_search(self):
        try:
            self.logger.debug("Click button search")
            self.get_element(self.BUTTON_SEARCH).click()
        except NoSuchElementException:
            self.logger.error("Button search not found")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            raise NoSuchElementException("Button search not found")

    @allure.step("Нажимаем на корзину")
    def click_button_cart(self):
        try:
            self.logger.debug("Click button cart")
            self.get_element(self.BUTTON_CART).click()
        except NoSuchElementException:
            self.logger.error("Button cart not found")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            raise NoSuchElementException("Button cart not found")
