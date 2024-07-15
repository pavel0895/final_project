from page_objects.registration_account import AccRegistration


def test_reg_acc(browser):
    AccRegistration(browser).open_registration_acc(browser)
    AccRegistration(browser).input_first_name("John")
    AccRegistration(browser).input_last_name("Doe")
    AccRegistration(browser).input_email("qwerty@example.com")
    AccRegistration(browser).input_password("123456")
    AccRegistration(browser).scroll_down_acc_registration()
    AccRegistration(browser).click_checkbox()
    AccRegistration(browser).click_submit_button()
