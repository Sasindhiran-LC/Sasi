import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.AccountPages import AccountPage
from pages.AddJobPage import AddJob
from pages.SearchPage import SearchPage
from test.BaseTest import BaseTest
from datetime import datetime
import time


@pytest.mark.usefixtures('setup_and_teardown',"log_on_failure")
class TestJobTitle(BaseTest):

    def test_add_job_title(self):
        self.driver.implicitly_wait(20)

        login_page = LoginPage(self.driver)
        # login_page.enter_email_id('Admin')
        # login_page.enter_password_id('admin123')
        # login_page.click_login_button()
        account_page = login_page.log_into_application('Admin','admin123')

        #account_page =AccountPage(self.driver)
        account_page.titel_of_page()
        time.sleep(5)

        search_page = SearchPage(self.driver)
        search_page.click_admin_module()
        time.sleep(3)

        add_job = AddJob(self.driver)
        # add_job.click_job_field()
        # add_job.click_job_title_field()
        # time.sleep(5)
        # add_job.click_add_button()
        # time.sleep(5)
        # add_job.enter_job_name(self.generate_job_tilte())
        # time.sleep(3)
        # add_job.click_save_button()

        add_job.add_job_(self.generate_job_tilte())




    def test_existing_job_title(self):

        login_page = LoginPage(self.driver)
        # login_page.enter_email_id('Admin')
        # login_page.enter_password_id('admin123')
        # login_page.click_login_button()

        account_page = login_page.log_into_application('Admin','admin123')

        # account_page = AccountPage(self.driver)
        account_page.titel_of_page()
        time.sleep(5)

        search_page = SearchPage(self.driver)
        search_page.click_admin_module()
        time.sleep(3)

        add_job = AddJob(self.driver)
        # add_job.click_job_field()
        # add_job.click_job_title_field()
        # time.sleep(3)
        # add_job.click_add_button()
        # add_job.enter_job_name('Automaton Tester')
        # time.sleep(3)
        # add_job.click_save_button()
        # time.sleep(3)
        add_job.add_job_('Automaton Tester')

        expected_job_title_warning = 'Already exists'


        assert add_job.retrieve_existing_warning().__contains__(expected_job_title_warning)
        time.sleep(3)



    def test_add_without_job_title(self):

        login_page = LoginPage(self.driver)
        # login_page.enter_email_id('Admin')
        # login_page.enter_password_id('admin123')
        # login_page.click_login_button()

        account_page = login_page.log_into_application('Admin','admin123')

        # account_page = AccountPage(self.driver)
        account_page.titel_of_page()
        time.sleep(5)

        search_page = SearchPage(self.driver)
        search_page.click_admin_module()
        time.sleep(3)

        add_job = AddJob(self.driver)
        # add_job.click_job_field()
        # add_job.click_job_title_field()
        # time.sleep(3)
        # add_job.click_add_button()
        # add_job.enter_job_name('')
        # add_job.click_save_button()
        add_job.add_job_('')

        expected_without_job_title_warning = 'Required'
        assert add_job.retrieve_without_warning().__contains__(expected_without_job_title_warning)
        time.sleep(3)



















