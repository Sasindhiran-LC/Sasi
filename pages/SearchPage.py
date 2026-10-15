import time

from selenium.webdriver.common.by import By
import time

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    admin_field_xpath = '(//span[normalize-space()="Admin"])[1]'
    search_username_field = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
    search_button_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    username_found_Xpath ="//span[@class='oxd-text oxd-text--span']"
    warning_message_xpath ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'


    def click_admin_module(self):
        self.driver.find_element(By.XPATH, self.admin_field_xpath).click()
        time.sleep(3)

    def enter_user_name(self,username_text):
        self.driver.find_element(By.XPATH, self.search_username_field).click()
        self.driver.find_element(By.XPATH,self.search_username_field).send_keys(username_text)
        time.sleep(3)

    def click_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()
        time.sleep(3)

    def user_name_fount_message(self):
        return self.driver.find_element(By.XPATH,self.username_found_Xpath).text

    def retrieve_user_warning_message(self):
        return self.driver.find_element(By.XPATH,self.warning_message_xpath).text

    def action_for_username_click_seacrh(self,username_text):
        self.click_admin_module()
        self.enter_user_name(username_text)
        self.click_search_button()





