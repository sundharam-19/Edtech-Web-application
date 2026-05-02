import pytest
from driver_factory import get_driver

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = get_driver(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()