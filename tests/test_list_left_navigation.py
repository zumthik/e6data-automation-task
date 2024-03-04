from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass

from pageObjects.LoginPage import Login
from pageObjects.WorkSpace import Workspace

class TestWorkspace(BaseClass):

    def test_list_of_left_navigation(self):

        login = Login(self.driver)
        login.login_using_valid_cre()

        workspace = Workspace(self.driver)
        workspace.workspace_details()
        workspace.get_left_navigation_list()