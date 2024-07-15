from page_objects.auth_admin_catalog import AdminCatalog
from page_objects.auth_admin_page import AuthAdmin
from page_objects.login_admin import LoginAdmin


def test_check_open_catalog(browser):
    AuthAdmin(browser).admin_acc(browser)
    AuthAdmin(browser).login("user", "bitnami")
    LoginAdmin(browser).click_submit_button()
    AdminCatalog(browser).click_menu_catalog()
    AdminCatalog(browser).click_products_list()
    AdminCatalog(browser).search_field_name()
