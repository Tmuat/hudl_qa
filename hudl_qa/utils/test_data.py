from utils import env


class TestData:
    # Global Variables
    CHROME_EXECUTABLE_PATH = env.chrome_executable_path
    BASE_URL = "https://www.hudl.com"

    # Login Page Variables
    LOGIN_TITLE = "Log In - Hudl"
    LOGIN_ERROR_TEXT = "We didn't recognize that email and/or password. Need help?"

    # Logged In Home Variables
    LOGGED_IN_TITLE = "Home - Hudl"
