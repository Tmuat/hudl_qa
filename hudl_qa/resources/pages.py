from locators import Locators


class BasePage:
    """
    This class is the base page and can be used by all other pages to
    expand from. It contains common functionality across all pages.
    """

    # This is called every time a new object of the base class is created to
    # create a new driver
    def __init__(self, driver):
        self.driver = driver
