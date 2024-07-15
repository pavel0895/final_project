from page_objects.auth_admin_page import AuthAdmin
from page_objects.login_admin import LoginAdmin


def test_login_admin(browser):
    AuthAdmin(browser).admin_acc(browser)
    LoginAdmin(browser).get_field_username_input
    LoginAdmin(browser).get_field_password_input
    LoginAdmin(browser).get_opencart_link
    LoginAdmin(browser).click_submit_button()
    LoginAdmin(browser).get_text_forgotten_password
