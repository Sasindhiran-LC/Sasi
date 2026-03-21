import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.AccountPages import AccountPage
import time

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:


    def test_login_with_vailed_credentials(self):

        login_page = LoginPage(self.driver)
        login_page.enter_email_id('Admin')
        login_page.enter_password_id('admin123')
        login_page.click_login_button()

        account_page = AccountPage(self.driver)
        account_page.titel_of_page()
        time.sleep(3)

    def test_login_with_invailed_credentials(self):

        login_page = LoginPage(self.driver)
        login_page.enter_email_id('Admisdn')
        login_page.enter_password_id('admin12ad3')
        login_page.click_login_button()

        expectedtext = 'Invalid credentials'
        time.sleep(3)
        assert login_page.retrieve_warning_message().__contains__(expectedtext)
        time.sleep(2)


    def test_login_without_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.enter_email_id('')
        login_page.enter_password_id('')
        login_page.click_login_button()

        expected_username_warning_message = 'Required'
        time.sleep(3)
        assert login_page.retrieve_username_warning_message().__contains__(expected_username_warning_message)

        expected_password_warning_message = 'Required'
        time.sleep(3)
        assert login_page.retrieve_password_warning_message().__contains__(expected_password_warning_message)






