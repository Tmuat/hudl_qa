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

# Third Party Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Local imports
from utils.test_data import TestData
from utils import env, locators


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
        self.driver.get(TestData.BASE_URL + "/login/")

        self.email = env.email
        self.incorrect_email = "Not_A_User@fakeemail.com"
        self.password = env.password
        self.incorrect_password = "WrongPassword"

        self.email_input = locators.Locators.EMAIL_INPUT
        self.password_input = locators.Locators.PASSWORD_INPUT
        self.submit = locators.Locators.SUBMIT_BUTTON

    def login(self):
        self.driver.find_element(By.ID, self.email_input).send_keys(self.email)
        self.driver.find_element(By.ID, self.password_input).send_keys(self.password)

        self.driver.find_element(By.ID, self.submit).click()

    def incorrect_email_login(self):
        self.driver.find_element(By.ID, self.email_input).send_keys(
            self.incorrect_email
        )
        self.driver.find_element(By.ID, self.password_input).send_keys(self.password)

        self.driver.find_element(By.ID, self.submit).click()

    def incorrect_password_login(self):
        self.driver.find_element(By.ID, self.email_input).send_keys(self.email)
        self.driver.find_element(By.ID, self.password_input).send_keys(
            self.incorrect_password
        )

        self.driver.find_element(By.ID, self.submit).click()

    def empty_email_and_password_login(self):
        self.driver.find_element(By.ID, self.submit).click()

    def empty_email_login(self):
        self.driver.find_element(By.ID, self.password_input).send_keys(self.password)

        self.driver.find_element(By.ID, self.submit).click()

    def empty_password_login(self):
        self.driver.find_element(By.ID, self.email_input).send_keys(
            self.incorrect_email
        )

        self.driver.find_element(By.ID, self.submit).click()

    def login_enter_key(self):
        self.driver.find_element(By.ID, self.email_input).send_keys(self.email)
        self.driver.find_element(By.ID, self.password_input).send_keys(self.password)

        self.driver.find_element(By.ID, self.submit).send_keys(Keys.RETURN)
