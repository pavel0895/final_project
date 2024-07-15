import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class LoginAdmin(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
        self.PASSWORD_INPUT = (By.NAME, "password")
        self.OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
        self.FORGOTTEN_PASSWORD = (By.XPATH, "//*[text()=' No match for Username and/or Password. ']")
        self.SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    @property
    @allure.step("Находим поле для ввода имени")
    def get_field_username_input(self):
        try:
            self.logger.info("Get field username input")
            return self.get_element(self.USERNAME_INPUT)
        except NoSuchElementException:
            self.logger.error("Field username input not found")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            raise NoSuchElementException("Field username input not found")

    @property
    @allure.step("Находим поле для ввода пароля")
    def get_field_password_input(self):
        try:
            self.logger.info("Get field password input")
            return self.get_element(self.PASSWORD_INPUT)
        except NoSuchElementException:
            self.logger.error("Field password input not found")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            raise NoSuchElementException("Field password input not found")

    @property
    @allure.step("Находим ссылку")
    def get_opencart_link(self):
        try:
            self.logger.info("Get opencart link")
            return self.get_element(self.OPENCART_LINK)
        except NoSuchElementException:
            self.logger.error("Opencart link not found")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            raise NoSuchElementException("Opencart link not found")

    @property
    @allure.step("Находим текст 'забыл пароль'")
    def get_text_forgotten_password(self):
        try:
            self.logger.info("Get text forgotten password")
            return self.get_element(self.USERNAME_INPUT)
        except NoSuchElementException:
            self.logger.error("Text forgotten password not found")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            raise NoSuchElementException("Text forgotten password not found")
