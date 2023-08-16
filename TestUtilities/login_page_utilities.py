import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from TestData import credentials
from TestLocators.login_page import LoginPageLocators


class LoginPageActions:

    def __init__(self):
        self.loginlocators = LoginPageLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def set_username(self):
        """
        find the webelement for username ,clear the text field and set the username passed

        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.loginlocators.username_locator_name_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)

    def set_password(self):
        """
        find the webelement for password ,clear the text field and set the username passed
        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.loginlocators.password_locator_name_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.loginlocators.login_button)
        login_button_webelement.click()

    def login_to_orangehrm(self):
        self.set_username()
        self.set_password()
        self.click_login()
        time.sleep(3)

    def login_success_message(self):
        return self.driver.title
