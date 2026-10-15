import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.AccountPages import AccountPage
from pages.SearchPage import SearchPage
import time
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class TestSearch:


    def test_search_valied_employee(self):

        login_page = LoginPage(self.driver)
        # login_page.enter_email_id('Admin')
        # login_page.enter_password_id('admin123')
        # login_page.click_login_button()

        account_page = login_page.log_into_application('Admin','admin123')

        # account_page = AccountPage(self.driver)
        account_page.titel_of_page()
        time.sleep(5)
        search_page = SearchPage(self.driver)
        # search_page.click_admin_module()
        # search_page.enter_user_name('Admin')
        # time.sleep(3)
        # search_page.click_search_button()

        search_page.action_for_username_click_seacrh('Admin')
        time.sleep(3)
        expected_user_name = '(1) Record Found'
        assert search_page.user_name_fount_message().__contains__(expected_user_name)

    def test_search_invalied_employee(self):

        login_page = LoginPage(self.driver)
        # login_page.enter_email_id('Admin')
        # login_page.enter_password_id('admin123')
        # login_page.click_login_button()

        account_page = login_page.log_into_application('Admin','admin123')

        # account_page = AccountPage(self.driver)
        account_page.titel_of_page()
        time.sleep(5)
        search_page = SearchPage(self.driver)
        # search_page.click_admin_module()
        # time.sleep(3)
        # search_page.enter_user_name('hfgasugfk')
        # time.sleep(3)
        # search_page.click_search_button()
        # time.sleep(3)
        search_page.action_for_username_click_seacrh('hfgasugfk')

        expected_warning_message = 'No Records Found'
        time.sleep(3)
        assert search_page.retrieve_user_warning_message().__contains__(expected_warning_message)
        time.sleep(3)







