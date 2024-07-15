from page_objects.auth_admin_catalog import AdminCatalog
from page_objects.auth_admin_page import AuthAdmin
from page_objects.delete_product_admin_section import DeleteProductAdminSection


def test_delete_product(browser):
    AuthAdmin(browser).admin_acc(browser)
    AuthAdmin(browser).login("user", "bitnami")
    AuthAdmin(browser).click_submit_button()
    AdminCatalog(browser).click_menu_catalog()
    AdminCatalog(browser).click_products_list()
    DeleteProductAdminSection(browser).click_checkbox()
    DeleteProductAdminSection(browser).click_delete_button()
