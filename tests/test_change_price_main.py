from page_objects.auth_admin_page import AuthAdmin
from page_objects.change_price_catalog import PriceCatalog
from page_objects.change_price_main import PriceMain


def test_change_price_main(browser):
    AuthAdmin(browser).open(browser)
    product_price_dollar = PriceMain(browser).get_price_dollar()
    PriceCatalog(browser).get_price_change_dollar(product_price_dollar)
    PriceCatalog(browser).get_change_currency()
    PriceMain(browser).get_pound_currency()
    product_price_pound_sterling = PriceMain(browser).get_price_pound()
    PriceMain(browser).get_price_change_pound(product_price_pound_sterling)
    assert PriceCatalog.check_price, "Цены изменились при переключении валюты"
