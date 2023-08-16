from TestUtilities.delete_employee_utilities import DeleteEmployeeActions


class PimDelete:

    def __init__(self):
        pass

    def test_pim_delete(self):
        """
        test case to test the user should be able to delete existing employee in PIM module
        :return:
        """

        _expected_message = "Successfully Deleted"
        DeleteEmployeeActions().delete_employee_information()
        assert DeleteEmployeeActions().delete_success_message() == _expected_message
        print("Successfully deleted")

PimDelete().test_pim_delete()