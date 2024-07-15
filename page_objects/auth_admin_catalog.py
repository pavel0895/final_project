import allure
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class AdminCatalog(BasePage):

    def __init__(self, browser):
        self.logger = browser.logger
        self.browser = browser
        self.MENU_CATALOG = (By.XPATH, "//*[@id ='menu-catalog']")
        self.PRODUCTS_LIST = (By.XPATH, "//*[@id ='collapse-1']/li[2]")
        self.FILTER_NAME = (By.XPATH, "//*[@id = 'input-name']")

    @allure.step("Открываем меню каталог")
    def click_menu_catalog(self):
        try:
            self.logger.info("Click menu catalog")
            self.get_element(self.MENU_CATALOG).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Выбираем продукт")
    def click_products_list(self):
        try:
            self.logger.info("Click products list")
            self.get_element(self.PRODUCTS_LIST).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Находим поле для ввода имени")
    def search_field_name(self):
        try:
            self.logger.info("Search field name")
            self.get_element(self.FILTER_NAME)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
