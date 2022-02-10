import time

import pytest

from TestData.LoginPageData import LoginPageData
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):

    def test_Login(self, getData):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)

        log.info("Username is " + getData["username"])
        loginpage.getemailId().send_keys(getData["username"])
        loginpage.getPassword().send_keys(getData["password"])
        loginpage.getLoginButton().click()
        self.waitForElementByXpath("//h2[contains(text(),'Add New Card')]")
        currentUrl = loginpage.getCurrentUrl()
        log.info(f"Login Successful")
        assert currentUrl == "https://webapp.kidzbery.com/FacePay/welcome.xhtml", "Login Unsuccessful"

    @pytest.fixture(params=LoginPageData.test_Login_data)
    def getData(self, request):
        return request.param
