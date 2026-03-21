from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver


    def titel_of_page(self):

        title = self.driver.title
        if title == "OrangeHRM":
            assert True
        else:
            assert False


