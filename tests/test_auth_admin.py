from page_objects.auth_admin_page import AuthAdmin


def test_auth_admin(browser):
    AuthAdmin(browser).admin_acc(browser)
    AuthAdmin(browser).login("user", "bitnami")
    AuthAdmin(browser).click_submit_button()
    assert AuthAdmin(browser).find_username.is_displayed()
    AuthAdmin(browser).logout()
