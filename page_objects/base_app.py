from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    path = "/administration"

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__
        self.USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
        self.PASSWORD_INPUT = (By.NAME, "password")
        self.SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def get_element(self, locator: tuple, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def get_all_elements(self, locator: tuple, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))

    def open(self, browser):
        self.logger.info("Successfully opened url: %s" % browser.base_url)
        self.logger.warning("Access denied")
        self.browser.get(browser.base_url)

    def admin_acc(self, browser):
        self.logger.info("Successfully opened url: %s" % browser.base_url + self.path)
        self.logger.warning("Access denied")
        self.browser.get(browser.base_url + self.path)

    def login(self, user, password):
        self.logger.info("Successful login")
        self.get_element(self.USERNAME_INPUT).send_keys(user)
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    def click_submit_button(self):
        self.get_element(self.SUBMIT_BUTTON).click()
