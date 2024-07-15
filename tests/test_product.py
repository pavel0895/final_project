from page_objects.auth_admin_page import AuthAdmin
from page_objects.product_card import ProductCard


def test_product_card(browser):
    AuthAdmin(browser).open(browser)
    ProductCard(browser).get_tablets_link()
    ProductCard(browser).get_tablets_check()
    ProductCard(browser).get_price_check
    ProductCard(browser).get_quantity_field
    ProductCard(browser).click_button_cart()
