import time

import pytest
from selenium import webdriver
from utilities import Readconfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = Readconfigurations.read_configuration("basic info", "browser")
    # By default it will run by chrome
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")

    driver.maximize_window()
    time.sleep(5)
    app_url = Readconfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    time.sleep(5)
    request.cls.driver = driver
    time.sleep(5)
    yield
    driver.quit()