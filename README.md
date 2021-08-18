# HUDL - QA Test

## Description

- Setup an automation environment on your local machine using selenium
- Automate any cases that you would think are good to test the functionality of validating logging into hudl.com with your credentials.
- Push your tests to a Github repository (a public repo is fine) and share the link (please do not include any passwords in public repos).

## Running Tests

**Set environment variables:**

- The project uses a number of environment variables to keep sensitive information hidden.
- An example of the env.py is located in the utils folder. To make the project work you will need to provide:
  - email
  - password
  - chrome_executable_path

**Running tests**

- Once inside the hudl_qa folder, the following command can be used to run the tests.
  - `python -m unittest -v hudl_qa.tests.all_tests.Test_HUDL_Login`
