import allure
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class AuthAdmin(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = self.__class__.__name__
        self.AUTH_LINK = (By.XPATH, '//span[contains(text(), "John Doe")]')
        self.LOGOUT_LINK = (By.XPATH, '//span[contains(text(), "Logout")]')
        self.SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
        self.USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
        self.PASSWORD_INPUT = (By.NAME, "password")

    @property
    @allure.step("Поиск имени юзера")
    def find_username(self):
        try:
            self.logger.info("Getting username")
            return self.get_element(self.AUTH_LINK)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Выходим из ЛК")
    def logout(self):
        try:
            self.logger.info("Logging out")
            self.get_element(self.LOGOUT_LINK).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
