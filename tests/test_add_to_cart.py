from page_objects.add_to_cart import AddCart
from page_objects.auth_admin_page import AuthAdmin


def test_add_to_cart(browser):
    AuthAdmin(browser).open(browser)
    AddCart(browser).set_window()
    AddCart(browser).add_product()
    AddCart(browser).success_alert()
