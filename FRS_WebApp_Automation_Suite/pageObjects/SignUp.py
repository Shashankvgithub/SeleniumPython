import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SignUp:

    def __init__(self, driver):
        self.driver = driver

    email_id=(By.ID,"signUpEmail")
    fname=(By.ID,"signUpFirstName")
    lname=(By.ID,"signUpLastName")
    mob=(By.ID,"signUpMobileNumber")
    dob=(By.ID,"signUpDateOfBirth")
    dob1=(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr[1]/td[4]/a")
    password=(By.ID,"newPassword")
    confpassword=(By.ID,"newCnfPassword")
    termscheck=(By.ID,"signup_checkbox")
    registerbutton=(By.ID,"btn_submit_details")
    cancelButton=(By.ID,"cancel_button")
    user_exist=(By.XPATH,"//li[contains(text(),'User already exist')]")

    def getEmailId(self):
        return self.driver.find_element(*SignUp.email_id)
    def getFirstName(self):
        return self.driver.find_element(*SignUp.fname)
    def getLastName(self):
        return self.driver.find_element(*SignUp.lname)
    def getMobile(self):
        return self.driver.find_element(*SignUp.mob)
    def clickDOBField(self):
        return self.driver.find_element(*SignUp.dob)
    def getUserExistTextField(self):
        return self.driver.find_element(*SignUp.user_exist)
    def getCancelButton(self):
        return self.driver.find_element(*SignUp.cancelButton)

    def select_date(self,d,m,y):
        self.driver.find_element(*SignUp.dob).click()
        year=Select(self.driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
        year.select_by_visible_text(y)

        month = Select(self.driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
        month.select_by_visible_text(m)

        dates = self.driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
        for i in dates:
            if i.text==d:
                i.click()



    def getEnterPassword(self):
        return self.driver.find_element(*SignUp.password)
    def getConfirmPassword(self):
        return self.driver.find_element(*SignUp.confpassword)
    def getCheckBox(self):
        return self.driver.find_element(*SignUp.termscheck)
    def getRegisterButton(self):
        return self.driver.find_element(*SignUp.registerbutton)

    def checkIfDislayed(self,xpath):
        return self.driver.find_element(By.XPATH,xpath).is_displayed()




#
# Date :
#
# //table[@class="ui-datepicker-calendar"]/tbody/tr/td/a
#
# Month:
#
# //select[@class="ui-datepicker-month"]/option
#
# Year:
#
# //select[@class="ui-datepicker-year"]/option

