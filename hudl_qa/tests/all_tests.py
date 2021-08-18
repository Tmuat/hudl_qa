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
from selenium.webdriver.common.by import By

# Local Imports
from pages.pages import LoginPage
from utils.locators import Locators
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

        time.sleep(4)
        self.assertIn(TestData.LOGGED_IN_TITLE, self.loginpage.driver.title)

    def test_003_incorrect_email(self):
        """
        Assert if the wrong email is passed, the user cannot login and
        an error message will be shown.
        """
        self.loginpage = LoginPage(self.driver)
        self.loginpage.incorrect_email_login()
        time.sleep(2)
        if (
            len(
                self.loginpage.driver.find_elements(
                    By.CLASS_NAME, Locators.ERROR_LOCATOR
                )
            )
            > 0
        ):
            element_found = True
        else:
            element_found = False
        self.assertTrue(element_found)

    def test_004_empty_email_and_password(self):
        """
        Assert if no email and password is passed, the user cannot
        login and an error message will be shown.
        """
        self.loginpage = LoginPage(self.driver)
        self.loginpage.empty_email_and_password_login()
        time.sleep(2)
        if (
            len(
                self.loginpage.driver.find_elements(
                    By.CLASS_NAME, Locators.ERROR_LOCATOR
                )
            )
            > 0
        ):
            element_found = True
        else:
            element_found = False
        self.assertTrue(element_found)

    def test_005_empty_email(self):
        """
        Assert if no email is passed, the user cannot
        login and an error message will be shown.
        """
        self.loginpage = LoginPage(self.driver)
        self.loginpage.empty_email_login()
        time.sleep(2)
        if (
            len(
                self.loginpage.driver.find_elements(
                    By.CLASS_NAME, Locators.ERROR_LOCATOR
                )
            )
            > 0
        ):
            element_found = True
        else:
            element_found = False
        self.assertTrue(element_found)

    def test_006_empty_password(self):
        """
        Assert if no password is passed, the user cannot
        login and an error message will be shown.
        """
        self.loginpage = LoginPage(self.driver)
        self.loginpage.empty_password_login()
        time.sleep(2)
        if (
            len(
                self.loginpage.driver.find_elements(
                    By.CLASS_NAME, Locators.ERROR_LOCATOR
                )
            )
            > 0
        ):
            element_found = True
        else:
            element_found = False
        self.assertTrue(element_found)

    def test_007_incorrect_password(self):
        """
        Assert if the wrong password is passed, the user cannot login and
        an error message will be shown.
        """
        self.loginpage = LoginPage(self.driver)
        self.loginpage.incorrect_password_login()
        time.sleep(2)
        if (
            len(
                self.loginpage.driver.find_elements(
                    By.CLASS_NAME, Locators.ERROR_LOCATOR
                )
            )
            > 0
        ):
            element_found = True
        else:
            element_found = False
        self.assertTrue(element_found)

    def test_008_error_text(self):
        """
        Assert if the correct error text is shown when a login error
        occurs.
        """
        self.loginpage = LoginPage(self.driver)
        self.loginpage.incorrect_password_login()
        time.sleep(2)
        error_text = self.loginpage.driver.find_element(
            By.XPATH, Locators.ERROR_TEXT_LOCATOR
        ).text
        self.assertEqual(TestData.LOGIN_ERROR_TEXT, error_text)

    def test_009_password_input_type(self):
        """
        Assert that the password input type is password and therefore
        masked.
        """
        self.loginpage = LoginPage(self.driver)
        if (
            len(self.loginpage.driver.find_elements(By.XPATH, Locators.PASSWORD_TYPE))
            > 0
        ):
            element_found = True
        else:
            element_found = False
        self.assertTrue(element_found)
