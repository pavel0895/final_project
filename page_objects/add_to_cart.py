import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class AddCart(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.logger = browser.logger
        self.class_name = self.__class__.__name__
        self.ADD_CART = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]")
        self.SUCCESS_ALERT = (By.CSS_SELECTOR, '.alert-success')

    def set_window(self):
        try:
            self.logger.info("changing the screen resolution")
            self.browser.set_window_size(1920, 1080)
        except Exception as e:
            self.logger.error(f"Error occurred while changing the screen resolution: {e}")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Добавляем продукт в корзину")
    def add_product(self):
        try:
            self.logger.info("Add product")
            product = self.get_element(self.ADD_CART)
            actions = ActionChains(self.browser)
            actions.move_to_element(product).perform()
            product.click()
            return product
        except Exception as e:
            self.logger.error(f"An error occurred while adding the product: {e}")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Получаем успешный алерт после добавления продукта")
    def success_alert(self):
        try:
            self.logger.info("Get success alert")
            self.get_element(self.SUCCESS_ALERT)
        except Exception as e:
            self.logger.error(f"An error occurred while getting the success alert: {e}")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
