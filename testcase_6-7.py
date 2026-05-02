from pages.login_page import LoginPage

def test_valid_login(driver):
    driver.get("https://www.guvi.in/login")
    login = LoginPage(driver)
    login.login("valid@email.com", "validpassword")
    assert "dashboard" in driver.current_url

def test_invalid_login(driver):
    driver.get("https://www.guvi.in/login")
    login = LoginPage(driver)
    login.login("wrong@email.com", "wrongpass")
    assert "invalid" in login.get_error().lower()