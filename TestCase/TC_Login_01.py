from TestUtilities.login_page_utilities import LoginPageActions


class TestLogin:

    def __init__(self):
        pass

    def tests_login_page(self):
        """
        test case to test the success message with valid credentials of our webpage
        :return:
        """
        _expected_message = "OrangeHRM"
        LoginPageActions().login_to_orangehrm()
        assert LoginPageActions().login_success_message() == _expected_message

TestLogin().tests_login_page()
