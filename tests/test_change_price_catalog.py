from page_objects.change_price_catalog import PriceCatalog


def test_change_price_catalog_desktops(browser):
    PriceCatalog(browser).open_catalog(browser)
    product_price_dollar = PriceCatalog(browser).get_product_price_dollar()
    PriceCatalog(browser).get_price_change_dollar(product_price_dollar)
    PriceCatalog(browser).get_change_currency()
    PriceCatalog(browser).get_euro_currency()
    product_price_euro = PriceCatalog(browser).get_product_price_euro()
    PriceCatalog(browser).get_price_change_euro(product_price_euro)
    assert PriceCatalog.check_price, "Цены изменились при переключении валюты"
