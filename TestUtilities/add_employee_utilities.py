from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from TestData import credentials
from TestLocators.add_employee import AddEmployeeLocators


class AddEmployeeActions:

    def __init__(self):
        self.addlocators = AddEmployeeLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url1)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def set_username(self):
        """
        find the webelement for username ,clear the text field and set the username passed

        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.addlocators.username_locator_name_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)

    def set_password(self):
        """
        find the webelement for password ,clear the text field and set the username passed
        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.addlocators.password_locator_name_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.addlocators.login_button)
        login_button_webelement.click()

    def pim(self):
        pim_webelement = self.driver.find_element(By.XPATH, self.addlocators.pim_module)
        pim_webelement.click()

    def add_employee_information(self):
        """
        find the webelement for employee to add new employee
        :return:
        """

        self.login_to_orangehrm()

        add_employee_webelement = self.driver.find_element(By.XPATH, self.addlocators.add_employee_button)
        add_employee_webelement.click()

        first_name_webelement = self.driver.find_element(By.XPATH, self.addlocators.employee_first_name)
        first_name_webelement.clear()
        first_name_webelement.send_keys(credentials.employee_first_name)

        last_name_webelement = self.driver.find_element(By.XPATH, self.addlocators.employee_last_name)
        last_name_webelement.clear()
        last_name_webelement.send_keys(credentials.employee_last_name)
        sleep(3)

        save_button_webelement = self.driver.find_element(By.XPATH, self.addlocators.employee_save_button)
        save_button_webelement.click()
        sleep(10)

    def login_to_orangehrm(self):
        self.set_username()
        self.set_password()
        self.click_login()
        sleep(3)

    def add_success_message(self):
        return "Successfully Saved"
