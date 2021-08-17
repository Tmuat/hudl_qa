# Standard library imports
import inspect
import os
import sys

# Used to get the current directory of this file
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# Extract path to the parent dir
parentdir = os.path.dirname(currentdir)
# Insert the path to the other folders
sys.path.insert(0, parentdir)

# Local imports
from utils.test_data import TestData


class BasePage:
    """
    This class is the base page and can be used by all other pages to
    expand from. It contains common functionality across all pages.
    """

    # This is called every time a new object of the base class is created to
    # create a new driver
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    """
    Home Page for HUDL.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


class LoginPage(BasePage):
    """
    Login Page for HUDL.
    """

    def __init__(self, driver):
        super().__init__(driver)
