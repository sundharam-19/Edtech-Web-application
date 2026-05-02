def test_menu_items(driver):
    page = HomePage(driver)
    page.open_url("https://www.guvi.in")
    assert page.is_courses_visible()