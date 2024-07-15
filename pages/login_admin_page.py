from selenium.webdriver.common.by import By


class LoginAdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.XPATH, "//*[text()=' No match for Username and/or Password. ']")
    AUTH_LINK = (By.XPATH, '//span[contains(text(), "John Doe")]')
    LOGOUT_LINK = (By.XPATH, '//span[contains(text(), "Logout")]')
