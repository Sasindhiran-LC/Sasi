from symtable import Class

from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_field_name = 'username'
    password_field_name = 'password'
    login_button_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    warning_message_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'
    expected_username_warning_message_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span'
    expected_password_warning_message_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span'


    def enter_email_id(self,email_text):
        self.driver.find_element(By.NAME, self.email_field_name).click()
        self.driver.find_element(By.NAME, self.email_field_name).clear()
        self.driver.find_element(By.NAME, self.email_field_name).send_keys(email_text)

    def enter_password_id(self, password_text):
        self.driver.find_element(By.NAME, self.password_field_name).click()
        self.driver.find_element(By.NAME, self.password_field_name).clear()
        self.driver.find_element(By.NAME, self.password_field_name).send_keys(password_text)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def retrieve_warning_message(self):
        return self.driver.find_element(By.XPATH, self.warning_message_xpath).text

    def retrieve_username_warning_message(self):
        return self.driver.find_element(By.XPATH,self.expected_username_warning_message_xpath).text

    def retrieve_password_warning_message(self):
        return self.driver.find_element(By.XPATH,self.expected_password_warning_message_xpath).text







