# from resources.locators import Locators
import test_data


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
