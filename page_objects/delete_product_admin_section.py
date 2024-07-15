import allure
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class DeleteProductAdminSection(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.CHECKBOX = (By.XPATH, "//*[@id = 'form-product']/div[1]/table/tbody/tr[1]/td[1]/input")
        self.DELETE_BUTTON = (By.XPATH, "//i[@class='fa-regular fa-trash-can']")

    @allure.step("Нажимаем на чек-бокс")
    def click_checkbox(self):
        try:
            self.logger.info("Click checkbox")
            self.browser.find_element(self.CHECKBOX).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Нажимаем на кнопку 'удалить'")
    def click_delete_button(self):
        try:
            self.logger.info("Click delete button")
            self.browser.find_element(self.DELETE_BUTTON).click()
        except Exception as e:
            self.logger.error(e)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
