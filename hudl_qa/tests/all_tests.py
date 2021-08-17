# Standard library imports
import inspect
import os
import sys
import time
import unittest

# Used to get the current directory of this file
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# Insert the path to the other folders
sys.path.insert(0, parentdir)

# Third Party Imports
from selenium import webdriver

# Local Imports
from pages.pages import LoginPage
from utils.test_data import TestData


# Creating a base class for all tests to use
class Test_HUDL_Base(unittest.TestCase):
    def setUp(self):
        """
        Defining and setting up how we want to run Selinium.
        Including maximising the window.
        """
        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
        self.driver.maximize_window()

    def tearDown(self):
        """
        After each test has executed cleanup ready for another test.
        """
        self.driver.close()
        self.driver.quit()


class Test_HUDL_Login(Test_HUDL_Base):
    """
    Testing HUDL Login.
    """

    def setUp(self):
        super().setUp()

    def test_001_login_page_loaded_successfully(self):
        """
        Assert if 'Log In - Hudl' is in the page title
        """
        self.loginpage = LoginPage(self.driver)
        self.assertIn(TestData.LOGIN_TITLE, self.loginpage.driver.title)

    def test_002_login_successfull(self):
        """
        Assert if with the right credentials you can login to the site.
        """
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login()
        time.sleep(3)
        self.assertIn(TestData.LOGGED_IN_TITLE, self.loginpage.driver.title)
