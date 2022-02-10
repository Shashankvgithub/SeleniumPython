from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_id = (By.ID, "bcId")
    password = (By.ID, "password")
    login_button = (By.ID, "continue")
    signup_button = (By.ID, "showCaptureBtn")
    forgotpwd_button = (By.XPATH, "//span[contains(text(),'Forgot password ?')]")

    def getemailId(self):
        return self.driver.find_element(*LoginPage.email_id)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLoginButton(self):
        return self.driver.find_element(*LoginPage.login_button)

    def getSignupButton(self):
        return self.driver.find_element(*LoginPage.signup_button)

    def getForgotPwdButton(self):
        return self.driver.find_element(*LoginPage.forgotpwd_button)

    def getCurrentUrl(self):
        return self.driver.current_url
