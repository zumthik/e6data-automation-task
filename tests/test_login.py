import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass

from pageObjects.LoginPage import Login


class TestLogin(BaseClass):

    def test_option_in_left_navigation(self):

        login = Login(self.driver)
        login.login_using_valid_cre()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
        "//td//a[@class='hyperlink-cls' and contains(text(), 'plt-infra')]")))

        # self.driver.find_element(By.XPATH, "//td//a[@class='hyperlink-cls' and contains(text(), 'plt-infra')]").click()
        self.driver.find_element(By.LINK_TEXT, "plt-infra").click()
        # optt =self.driver.find_elements(By.XPATH, "//a[contains(@href,'workspace-details')]//parent::li")
        left_nav =self.driver.find_elements(By.XPATH, "//div[@class='left-nav collapsed ']//ul//li")
        print(len(left_nav))
        for option in left_nav:
            print(option.text.strip())
        time.sleep(4)







