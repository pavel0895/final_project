import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class AccRegistration(BasePage):
    path = "/index.php?route=account/register"

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.FIRST_NAME = (By.XPATH, "//*[@id='input-firstname']")
        self.LAST_NAME = (By.XPATH, "//*[@id='input-lastname']")
        self.EMAIL = (By.XPATH, "//*[@id='input-email']")
        self.PASSWORD_INPUT = (By.XPATH, "//*[@id='input-password']")
        self.CHECKBOX = (By.NAME, "agree")
        self.SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    @allure.step("Открываем страницу регистрации")
    def open_registration_acc(self, browser):
        try:
            self.logger.info("Open registration acc")
            self.browser.get(browser.base_url + self.path)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Вводим данные в поле 'имя'")
    def input_first_name(self, firstname):
        try:
            self.logger.info("Input first name")
            self.get_element(self.FIRST_NAME).send_keys(firstname)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Вводим данные в поле 'фамилия'")
    def input_last_name(self, lastname):
        try:
            self.logger.info("Input last name")
            self.get_element(self.LAST_NAME).send_keys(lastname)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Вводим данные в поле 'email'")
    def input_email(self, email):
        try:
            self.logger.info("Input email")
            self.get_element(self.EMAIL).send_keys(email)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Вводим данные в поле 'пароль'")
    def input_password(self, password):
        try:
            self.logger.info("Input password")
            self.get_element(self.PASSWORD_INPUT).send_keys(password)
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Нажимаем на чек-бокс")
    def click_checkbox(self):
        try:
            self.logger.info("Click checkbox")
            self.get_element(self.CHECKBOX).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Скролл страницы")
    def scroll_down_acc_registration(self):
        try:
            self.logger.info("Scroll down acc registration")
            product = self.get_element(self.CHECKBOX)
            actions = ActionChains(self.browser)
            actions.move_to_element(product).perform()
            product.click()
            return product
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
