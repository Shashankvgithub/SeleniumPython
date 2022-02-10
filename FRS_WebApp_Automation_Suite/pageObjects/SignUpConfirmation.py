import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SignUpConfirm:

    def __init__(self, driver):
        self.driver = driver

    confirmation_text=(By.XPATH,"//div[@class='welcome-screen']/div/div/div/h2")
    email_verification_text=(By.XPATH,"//div[@class='welcome-screen']/div/div/div/h4")


    def getConfirmationTextField(self):
        return self.driver.find_element(*SignUpConfirm.confirmation_text)
    def getEmailVerificationTextField(self):
        return self.driver.find_element(*SignUpConfirm.email_verification_text)