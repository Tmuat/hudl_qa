# Standard library imports
import inspect
import os
import sys

# Used to get the current directory of this file
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# Insert the path to the other folders
sys.path.insert(0, parentdir)

# Third Party Imports
from selenium import webdriver

# Local Imports
from utils.test_data import TestData


def setup():
    return webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)


def logintest():
    driver = setup()

    driver.get("https://www.hudl.com/login")
    driver.set_page_load_timeout(30)

    driver.quit()


if __name__ == "__main__":
    logintest()
