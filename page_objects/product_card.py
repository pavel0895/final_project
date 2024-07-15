import allure
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class ProductCard(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.logger = browser.logger
        self.TABLETS_LINK = (By.LINK_TEXT, "Tablets")
        self.TABLETS_CHECK = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
        self.PRICE_CHECK = (By.CLASS_NAME, "price-new")
        self.QUANTITY_FIELD = (By.XPATH, "//*[@id ='input-quantity']")
        self.BUTTON_CART = (By.XPATH, "//*[@id ='button-cart']")

    def get_tablets_link(self):
        try:
            self.logger.info("Get tablets link")
            self.browser.find_element(self.TABLETS_LINK).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    def get_tablets_check(self):
        try:
            self.logger.info("Get tablets check")
            self.browser.find_element(self.TABLETS_CHECK).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @property
    def get_price_check(self):
        try:
            self.logger.info("Get price check")
            return self.browser.find_element(self.PRICE_CHECK)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @property
    @allure.step("Находим поле 'количество'")
    def get_quantity_field(self):
        try:
            self.logger.info("Get quantity field")
            return self.browser.find_element(self.QUANTITY_FIELD)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Добавляем пордукт в корзину")
    def click_button_cart(self):
        try:
            self.logger.info("Click button cart")
            self.browser.find_element(self.BUTTON_CART).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
