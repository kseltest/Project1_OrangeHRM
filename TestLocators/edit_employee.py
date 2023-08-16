class EditEmployeeLocators:
    def __init__(self):
        pass

    username_locator_name_tag = "username"
    password_locator_name_tag = "password"
    login_button = '//button[@type="submit"]'
    pim_module = '//a[@href="/web/index.php/pim/viewPimModule"]'
    employee_name = '//div[@class ="oxd-autocomplete-text-input oxd-autocomplete-text-input--active"]'
    employee_name1 = '// input[@placeholder = "Type for hints..."]'
    search_button = '//button[@type="submit"]'
    select_employee_checkbox = '//i[@class="oxd-icon bi-check oxd-checkbox-input-icon"]'
    employee_edit_icon = '//i[@class="oxd-icon bi-pencil-fill"]'
    employee_edit_name = '//input[@name="firstName"]'
    save_button = '//button[@type="submit"]'
