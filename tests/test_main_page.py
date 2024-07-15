from page_objects.auth_admin_page import AuthAdmin
from page_objects.main_page import MainPage


def test_check_main(browser):
    AuthAdmin(browser).open(browser)
    MainPage(browser).get_link_opencart
    MainPage(browser).get_search_field
    MainPage(browser).click_button_search()
    MainPage(browser).click_button_cart()
    MainPage(browser).get_currency_form
