from selenium.webdriver.common.by import By


class CatalogPage:
    LOGIN_INPUT = (By.XPATH, "//*[@id ='input-username']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id ='input-password']")
    MENU_CATALOG = (By.XPATH, "//*[@id ='menu-catalog']")
    PRODUCTS_LIST = (By.XPATH, "//*[@id ='collapse-1']/li[2]")
    FILTER_NAME = (By.XPATH, "//*[@id = 'input-name']")
    MODEL_NAME = (By.XPATH, "//*[@] = 'input-model']")
    FILTER_PRICE = (By.XPATH, "//*[@id = 'input-price']")
