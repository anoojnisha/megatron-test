import pytest
from selenium.webdriver import chrome, firefox

def get_driver_instance():
    browser = pytest.config.option.type.lower()
    if browser =='chrome':
        driver =chrome("./browser-server/chromedriver.exe")
    elif browser =='firefox':
        driver = firefox("./browser-server/geckodriver.exe")
    else:
        print('Invalid Browser Option')
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("http://localhost")
    return driver

