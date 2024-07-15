from selenium.webdriver.common.by import By


class CheckMainPage:
    CURRENCY_FORM = (By.XPATH, "//*[@id='form-currency']/div/a/span")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button[type='button']")
    SEARCH_FIELD = (By.XPATH, "//*[@id='search']")
    LINK_OPENCART = (By.LINK_TEXT, "Specials")
    BUTTON_CART = (By.XPATH, "//*[@id='header-cart']/div/button")
    ADD_CART = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]")
    ADD_BASKET = (By.XPATH, "//*[@id ='alert']/div/text()[1]")
    SUCCESS_ALERT = (By.CSS_SELECTOR, '.alert-success')
    CHANGE_CURRENCY = (By.XPATH, "//span[contains(text(), 'Currency')]")
    PRODUCT_LIST = (By.ID, "product-list")
    EURO_CURRENCY = (By.LINK_TEXT, "€ Euro")
    POUND_CURRENCY = (By.LINK_TEXT, "£ Pound Sterling")
    MAIN_PRODUCTS = (By.ID, "content")
