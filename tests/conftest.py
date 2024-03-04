import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class', autouse=True)
def setup(request):
    """initialise the driver
    load the url
    maximize the window
    """
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://friends1.e6xlabs.cloud/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()