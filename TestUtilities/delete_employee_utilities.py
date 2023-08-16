from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from TestData import credentials

from TestLocators.delete_employee import DeleteEmployeeLocators
from TestUtilities.login_page_utilities import LoginPageActions


class DeleteEmployeeActions:

    def __init__(self):
        self.deletelocators = DeleteEmployeeLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url1)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def set_username(self):
        """
        find the webelement for username ,clear the text field and set the username passed

        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.deletelocators.username_locator_name_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)

    def set_password(self):
        """
        find the webelement for password ,clear the text field and set the username passed
        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.deletelocators.password_locator_name_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.deletelocators.login_button)
        login_button_webelement.click()

    def pim(self):
        pim_webelement = self.driver.find_element(By.XPATH, self.deletelocators.pim_module)
        pim_webelement.click()

    def delete_employee_information(self):
        """
        find the webelement for employee to select and delete the existing empolyee
        :return:
        """
        LoginPageActions.login_to_orangehrm(self)
        print(self.driver.current_url)

        select_button_webelement = self.driver.find_element(By.XPATH, self.deletelocators.employee_select_button)
        select_button_webelement.is_selected()
        sleep(2)

        delete_button_webelement = self.driver.find_element(By.XPATH, self.deletelocators.employee_delete_button)
        delete_button_webelement.click()
        sleep(5)

        delete_option_webelement = self.driver.find_element(By.XPATH,self.deletelocators.delete_option)
        delete_option_webelement.click()
        sleep(5)

    def login_to_orangehrm(self):
        self.set_username()
        self.set_password()
        self.click_login()
        sleep(3)

    def delete_success_message(self):
        success_message = "Successfully Deleted"
        return success_message
