class DeleteEmployeeLocators:
    def __init__(self):
        pass

    username_locator_name_tag = "username"
    password_locator_name_tag = "password"
    login_button = '//button[@type="submit"]'
    pim_module = '//a[@href="/web/index.php/pim/viewPimModule"]'
    employee_select_button = '//input[@value="1"]'
    """ value gives the number of employee in the list--0 is first employee in the list"""
    employee_delete_button = '//i[@class ="oxd-icon bi-trash"]'
    popup_messagebox_for_deletion = '//div[@role="document"]'
    """ use drive.swtich_to_alert()--syntax for popup message box"""
    delete_option = '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'


