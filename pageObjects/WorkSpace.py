from datetime import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class Workspace:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    WORKSPACE_LANDING_PAGE = By.XPATH, "//td//a[@class='hyperlink-cls' and contains(text(), 'plt-infra')]",
    WORKSPACE_DETAILS_LINK = By.LINK_TEXT, "plt-infra",
    LEFT_BREADCRUMB = By.XPATH, "//a[contains(@href,'workspace-details')]",
    LEFT_NAVIGATION_OPTIONS = (By.XPATH, "//*[local-name()='svg' and @class='medium-icon']/*[local-name()='path']")

    def workspace_details(self):
        self.driver.find_element(*Workspace.WORKSPACE_DETAILS_LINK).click()

    def get_left_navigation_list(self):
        self.driver.find_element(*Workspace.LEFT_BREADCRUMB).click()
        opt = self.driver.find_elements(*Workspace.LEFT_NAVIGATION_OPTIONS)
        print(len(opt))










        #     self.driver.find_element(By.XPATH, "//a[contains(@href,'workspace-details')]").click()
        #     options = self.driver.find_elements(By.XPATH,
        #                                         "//*[local-name()='svg' and @class='medium-icon']/*[local-name()='path']")
        #
        #     print("Options in the left navigation:")
        #     for option in options:
        #         print(option.text.strip())
        # finally:
        #     self.driver.quit()