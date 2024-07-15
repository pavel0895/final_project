import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.base_app import BasePage


class AddNewProductAdminSection(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.WebDriverWait = None
        self.browser = browser
        self.LINK_ADD_NEW = (By.XPATH, "//i[@class='fa-solid fa-plus']")
        self.USERNAME_INPUT = (By.NAME, "product_description[1][name]")
        self.TAG_INPUT = (By.NAME, "product_description[1][meta_title]")
        self.TAB_DATA = (By.LINK_TEXT, "Data")
        self.MODEL_INPUT = (By.NAME, "model")
        self.TAB_SEO = (By.LINK_TEXT, "SEO")
        self.KEYWORD_INPUT = (By.NAME, "product_seo_url[0][1]")
        self.TAB_SEO = (By.LINK_TEXT, "SEO")
        self.SAVE = (By.XPATH, "//i[@class='fa-solid fa-floppy-disk']")
        self.SUCCESS_ALERT_PRODUCT = (By.CSS_SELECTOR, '.alert-success')
        self.logger = browser.logger

    @allure.step("Вводим название продукта")
    def input_product_name(self, product_name, USERNAME_INPUT):
        try:
            self.logger.info("Input product name")
            self.get_element(self.USERNAME_INPUT).send_keys(product_name)
        except Exception as e:
            self.logger.error("An error occurred while entering the product name")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Вводим модель продукта")
    def input_model_product(self, product_model):
        try:
            self.logger.info("Input product name")
            self.get_element(self.MODEL_INPUT).send_keys(product_model)
        except Exception as e:
            self.logger.error("An error occurred while entering the product name")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Вводим заголовок тэга")
    def input_tag_title(self, tag_title):
        try:
            self.logger.info("Input tag title")
            self.get_element(self.TAG_INPUT).send_keys(tag_title)
        except Exception as e:
            self.logger.error("An error occurred while entering the tag title")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Вводим ключевое слово")
    def input_keyword(self, keyword):
        try:
            self.logger.info("Input keyword")
            self.get_element(self.KEYWORD_INPUT).send_keys(keyword)
        except Exception as e:
            self.logger.error("An error occurred while entering the keyword")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Скролл страницы")
    def scroll_down_products(self):
        try:
            self.logger.info("Scroll down products")
            product = self.get_element(self.TAG_INPUT)
            actions = ActionChains(self.browser)
            actions.move_to_element(product).perform()
            product.click()
            return product
        except Exception as e:
            self.logger.error("An error occurred while scrolling down products")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Добавляем новый продукт")
    def click_add_new_product(self):
        try:
            self.logger.info("Click add new product")
            self.get_element(self.LINK_ADD_NEW).click()
        except Exception as e:
            self.logger.error("An error occurred while clicking add new product")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Вводим название продукта")
    def click_tab_data(self):
        try:
            self.logger.info("Click tab data")
            self.get_element(self.TAB_DATA).click()
        except Exception as e:
            self.logger.error("An error occurred while clicking tab data")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Переходим на вкладку Data")
    def click_tab_seo(self):
        try:
            self.logger.info("Click tab seo")
            self.get_element(self.TAB_SEO).click()
        except Exception as e:
            self.logger.error("An error occurred while clicking tab seo")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Сохраняем продукт")
    def click_save_product(self):
        try:
            self.logger.info("Click save product")
            self.get_element(self.SAVE).click()
        except Exception as e:
            self.logger.error("An error occurred while clicking save product")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @allure.step("Получаем успешный алерт после добавления продукта")
    def success_alert_product(self):
        try:
            self.logger.info("Success alert product")
            self.get_element(self.SUCCESS_ALERT_PRODUCT)
        except Exception as e:
            self.logger.error("An error occurred while success alert product")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
