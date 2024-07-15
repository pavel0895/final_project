import allure
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class PriceCatalog(BasePage):
    path = "/en-gb/catalog/desktops"

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.PRODUCT_LIST = (By.ID, "product-list")
        self.CHANGE_CURRENCY = (By.XPATH, "//span[contains(text(), 'Currency')]")
        self.EURO_CURRENCY = (By.LINK_TEXT, "€ Euro")

    @allure.step("Открываем каталог")
    def open_catalog(self, browser):
        try:
            self.logger.info("Open catalog")
            self.browser.get(browser.base_url + self.path)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Находим продукт")
    def get_product_price_dollar(self):
        try:
            self.logger.info("Get product price dollar")
            return self.get_all_elements(self.PRODUCT_LIST)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Сохраняем продукт в долларах")
    def get_price_change_dollar(self, product_price_dollar):
        try:
            self.logger.info("Get price change dollar")
            self.price_before_change = [price.text for price in product_price_dollar]
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Меняем валюту на евро")
    def get_change_currency(self):
        try:
            self.logger.info("Get change currency")
            self.get_element(self.CHANGE_CURRENCY).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    def get_euro_currency(self):
        try:
            self.logger.info("Get euro currency")
            self.get_element(self.EURO_CURRENCY).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Находим продукт в евро")
    def get_product_price_euro(self):
        try:
            self.logger.info("Get product price euro")
            return self.get_all_elements(self.PRODUCT_LIST)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Сохраняем продукт в евро")
    def get_price_change_euro(self, product_price_euro):
        try:
            self.logger.info("Get price change euro")
            self.price_after_change = [price.text for price in product_price_euro]
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @property
    @allure.step("Проверяем изменения валют")
    def check_price(self):
        try:
            self.logger.info("Check price")
            return self.price_after_change != self.price_before_change
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
