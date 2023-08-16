class AddEmployeeLocators:
    def __init__(self):
        pass

    username_locator_name_tag = "username"
    password_locator_name_tag = "password"
    login_button = '//button[@type="submit"]'
    pim_module = '//a[@href="/web/index.php/pim/viewPimModule"]'
    add_employee_button = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
    employee_first_name = '//input[@name="firstName"]'
    employee_last_name = '//input[@name="lastName"]'
    employee_save_button = '//button[@type="submit"]'