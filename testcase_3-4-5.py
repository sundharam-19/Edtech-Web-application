from pages.home_page import HomePage

def test_login_button(driver):
    page = HomePage(driver)
    page.open_url("https://www.guvi.in")
    assert page.find(page.LOGIN_BTN).is_displayed()

def test_signup_navigation(driver):
    page = HomePage(driver)
    page.open_url("https://www.guvi.in")
    page.click_signup()
    assert "register" in driver.current_ur