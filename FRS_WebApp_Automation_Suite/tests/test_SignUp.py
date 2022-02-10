import time

from pageObjects import SignUpConfirmation
from pageObjects.LoginPage import LoginPage
from pageObjects.SignUp import SignUp
from utilities.BaseClass import BaseClass


class TestSignUp(BaseClass):

    def test_signUp_register(self):
        try:
            log = self.getLogger()
            loginpage = LoginPage(self.driver)
            loginpage.getSignupButton().click()
            self.waitForElementByXpath("//input[@id='signUpEmail']")
            signuppage = SignUp(self.driver)
            signuppage.getEmailId().send_keys("shashank1234@gmail.com")
            log.info("Entered the Email Id")
            signuppage.getFirstName().send_keys("Shashank")
            log.info("Entered the FirstName")
            signuppage.getLastName().send_keys("Verma")
            log.info("Entered the Last Name")
            signuppage.getMobile().send_keys("98769875")
            log.info("Entered the Mobile Number")
            signuppage.clickDOBField().click()
            log.info("Clicked on the DOB Field")
            signuppage.select_date('15', 'Jul', '1989')
            log.info("Selected the Date")
            signuppage.getEnterPassword().send_keys("Abc@1234")
            log.info("Entered the password")
            signuppage.getConfirmPassword().send_keys("Abc@1234")
            log.info("Entered the confirm password")
            if not signuppage.getCheckBox().is_selected():
                signuppage.getCheckBox().click()
            log.info("Selected the Terms & Conditions Checkbox")
            signuppage.getRegisterButton().click()
            log.info("Clicked on the Register Button")
            signupconfirm = SignUpConfirmation.SignUpConfirm(self.driver)

            self.waitForElementByXpath("//div[@class='welcome-screen']/div/div/div/h2")
            log.info("Waiting for User to get registered")
            confirmText = signupconfirm.getConfirmationTextField().text
            log.info(confirmText)
            assert "User has been successfully registered" in confirmText

        except Exception as e:
            check_text_presence = signuppage.checkIfDislayed("//li[contains(text(),'User already exist')]")
            if check_text_presence == True:
                log.info("User Already Exist")
                assert False, "User already Exist"
            else:
                log.info(e)

    def test_signUp_cancel(self):
        try:
            log = self.getLogger()
            loginpage = LoginPage(self.driver)
            loginpage.getSignupButton().click()
            self.waitForElementByXpath("//input[@id='signUpEmail']")
            signuppage = SignUp(self.driver)
            signuppage.getCancelButton().click()
            log.info("Clicked on the Cancel Button")
            assert loginpage.getemailId().is_displayed(), "Unable to cancel the signup process"

        except Exception as e:
            log.info(e)
