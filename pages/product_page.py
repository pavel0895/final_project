from selenium.webdriver.common.by import By


class ProductPage:
    TABLETS_LINK = (By.LINK_TEXT, "Tablets")
    TABLETS_CHECK = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
    BUTTON_CART = (By.XPATH, "//*[@id ='button-cart']")
    QUANTITY_FIELD = (By.XPATH, "//*[@id ='input-quantity']")
    PRICE_CHECK = (By.CLASS_NAME, "price-new")
