from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from TestData import credentials
from TestLocators.edit_employee import EditEmployeeLocators


class EditEmployeeActions:

    def __init__(self):
        self.editlocators = EditEmployeeLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url1)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def set_username(self):
        """
        find the webelement for username ,clear the text field and set the username passed

        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.editlocators.username_locator_name_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)

    def set_password(self):
        """
        find the webelement for password ,clear the text field and set the username passed
        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.editlocators.password_locator_name_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.editlocators.login_button)
        login_button_webelement.click()

    def pim(self):
        pim_webelement = self.driver.find_element(By.XPATH, self.editlocators.pim_module)
        pim_webelement.click()

    def employee_information(self):
        """
        find the webelement for employee to select and edit the information and then safe the details
        :return:
        """
        self.login_to_orangehrm()

        employee_name1_webelement = self.driver.find_element(By.XPATH, self.editlocators.employee_name1)
        employee_name1_webelement.clear()
        employee_name1_webelement.send_keys(credentials.employee_name1)
        sleep(5)

        select_employee_webelement = self.driver.find_elements(By.XPATH, self.editlocators.select_employee_checkbox)
        select_employee_webelement[1].click()

        edit_employee_webelement = self.driver.find_element(By.XPATH, self.editlocators.employee_edit_icon)
        edit_employee_webelement.click()
        sleep(5)

        edit_employee_webelement = self.driver.find_element(By.XPATH, self.editlocators.employee_edit_name)
        edit_employee_webelement.clear()
        edit_employee_webelement.send_keys(credentials.employee_edit_name)

        save_button_webelement = self.driver.find_element(By.XPATH, self.editlocators.save_button)
        save_button_webelement.click()
        sleep(2)

    def login_to_orangehrm(self):
        self.set_username()
        self.set_password()
        self.click_login()
        sleep(3)

    def edit_success_message(self):
        success_message = "Successfully Updated"
        return success_message
