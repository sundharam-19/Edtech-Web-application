def test_homepage_load(driver):
    driver.get("https://www.guvi.in")
    assert "guvi" in driver.current_url.lower()

def test_title(driver):
    driver.get("https://www.guvi.in")
    assert driver.title == "GUVI | Learn to code in your native language"
