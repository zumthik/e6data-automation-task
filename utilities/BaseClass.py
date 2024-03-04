import pytest

import inspect
import logging

from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("login")
class BaseClass:

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        element_presence = self.wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element_presence

