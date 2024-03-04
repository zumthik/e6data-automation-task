from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from utilities.BaseClass import BaseClass


class Login:

    def __init__(self, driver):
        self.driver = driver

    # Login locators
    EMAIL_FIELD = By.XPATH, "//div[@class='form-floating']//input[@placeholder='Email']",
    PASSWORD_FIELD = By.XPATH, "//div[contains(@class, 'password-input')]//input[@placeholder='Password']",
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "div button[type='submit']")

    def login_using_valid_cre(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*Login.EMAIL_FIELD).send_keys("task@e6x.io")
        self.driver.find_element(*Login.PASSWORD_FIELD).send_keys("Abcd@123")
        self.driver.find_element(*Login.SIGN_IN_BUTTON).click()
        # driver.find_element(By.CSS_SELECTOR, "a[href*='workspace'])")