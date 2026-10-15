from selenium.webdriver.common.by import By
from test.BaseTest import BaseTest
from selenium import webdriver
import time

class AddJob:
    def __init__(self, driver):
        self.driver = driver



    job_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span'
    job_title_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]"
    add_button_xpath = "//button[normalize-space()='Add']"
    job_title_field_xpath = "//label[text()='Job Title']/following::input[1]"
    save_button_xpath = "//button[normalize-space()='Save']"
    job_title_warning = "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    without_job_title_warning = "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"


    time.sleep(3)
    def click_job_field(self):
        self.driver.find_element(By.XPATH,self.job_xpath).click()
        time.sleep(3)

    def click_job_title_field(self):
        self.driver.find_element(By.XPATH,self.job_title_xpath).click()
        time.sleep(3)

    def click_add_button(self):
        self.driver.find_element(By.XPATH,self.add_button_xpath).click()
        time.sleep(3)

    def enter_job_name(self,job_title_text):
        self.driver.find_element(By.XPATH,self.job_title_field_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.job_title_field_xpath).send_keys(job_title_text)
        time.sleep(3)

    def click_save_button(self):
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()
        time.sleep(3)

    def retrieve_existing_warning(self):
        return self.driver.find_element(By.XPATH,self.job_title_warning).text

    def retrieve_without_warning(self):
        return self.driver.find_element(By.XPATH,self.without_job_title_warning).text

    def add_job_(self,job_title_text):
        self.driver.implicitly_wait(20)
        self.click_job_field()
        time.sleep(3)
        self.click_job_title_field()
        time.sleep(3)
        self.click_add_button()
        time.sleep(3)
        self.enter_job_name(job_title_text)
        time.sleep(3)
        self.click_save_button()









