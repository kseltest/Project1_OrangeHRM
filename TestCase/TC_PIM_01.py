from TestUtilities.add_employee_utilities import AddEmployeeActions


class PimAdd:

    def __init__(self):
        pass

    def tests_pim_add(self):
        """
        test case to test the user should be able to add new employee in PIM module
        :return:
        """

        _expected_message = "Successfully Saved"
        AddEmployeeActions().add_employee_information()

        assert AddEmployeeActions().add_success_message() == _expected_message
        print("Successfully Saved")

PimAdd().tests_pim_add()