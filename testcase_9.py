def test_dobby_presence(driver):
    driver.get("https://www.guvi.in")
    assert "dobby" in driver.page_source.lower()