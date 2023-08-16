from TestUtilities.edit_employee_utilities import EditEmployeeActions


class PimEdit:

    def __init__(self):
        pass

    def test_pim_edit(self):
        """
        test case to test the user should be able to edit exiting employee information in PIM module
        and should see a success message of detail addition
        :return:
        """
        _expected_message = "Successfully Updated"

        EditEmployeeActions().employee_information()
        assert EditEmployeeActions().edit_success_message() == _expected_message
        print("Successfully Updated")

PimEdit().test_pim_edit()