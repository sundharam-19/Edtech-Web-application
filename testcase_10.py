def test_logout(driver):
    driver.get("https://www.guvi.in/login")
    # login steps here
    driver.find_element("xpath", "//button[text()='Logout']").click()
    assert "login" in driver.current_url.lower()