import inspect
import logging

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup')       #define fixture for setup method in conftest
class BaseClass:
    search = (By.CSS_SELECTOR, "input[type = 'search']")  # search option
    searchsuggestion = (By.CSS_SELECTOR, "span[class = 'aws_result_title']")

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        Filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s, %(levelname)s, %(name)s, %(message)s")
        Filehandler.setFormatter(formatter)
        logger.addHandler(Filehandler)
        logger.setLevel(logging.INFO)
        return logger

    def search_item(self):
        return self.driver.find_element(*BaseClass.search)  # calling search edit

    def Search_Suggestions(self):
        return self.driver.find_elements(*BaseClass.searchsuggestion)  # calling suggestions from dynamic drop down


