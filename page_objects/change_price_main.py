import allure
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class PriceMain(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.logger = browser.logger
        self.MAIN_PRODUCTS = (By.ID, "content")
        self.POUND_CURRENCY = (By.LINK_TEXT, "£ Pound Sterling")

    @allure.step("Находим продукт в долларах")
    def get_price_dollar(self):
        try:
            self.logger.info("Get price dollar")
            return self.get_all_elements(self.MAIN_PRODUCTS)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Меняем валюту на фунты стерлинги")
    def get_pound_currency(self):
        try:
            self.logger.info("Get pound currency")
            self.get_element(self.POUND_CURRENCY).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Находим продукт в фунтах стерлингах")
    def get_price_pound(self):
        try:
            self.logger.info("Get price pound")
            return self.get_all_elements(self.MAIN_PRODUCTS)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Сохраняем продукт в фунтах стерлингах")
    def get_price_change_pound(self, product_price_pound_sterling):
        try:
            self.logger.info("Get price change pound")
            self.price_after_change = [price.text for price in product_price_pound_sterling]
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
