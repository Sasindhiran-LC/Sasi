from selenium.webdriver.common.by import By
import time

class AddJob:
    def __init__(self, driver):
        self.driver = driver

    job_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span'
    job_title_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a'
    add_button_xpath = '//*[@id="app"]/di v[1]/div[2]/div[2]/div/div/div[1]/div/button'
    job_title_field_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    save_button_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]'
    job_title_warning = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/span'
    without_job_title_warning = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/span'


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









