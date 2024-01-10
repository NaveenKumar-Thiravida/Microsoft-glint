import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://app.vgqa.glint.cloud-dev.microsoft/session/auth"
    Email_address = "qatester@glintinc.com"
    Client_id = "qa20191108"
    Password = "Dem0@pass2"

    def test_LandingPageTitle(self,setup):
        self.driver = setup
        time.sleep(10)

        self.driver.get(self.baseURL)
        time.sleep(10)
        actual_title=self.driver.title

        if actual_title=="Authenticate - Viva Glint":
            assert True
        else:
            self.driver.save_screenshot("C:/Users/admin/PycharmProject/pythonProject/Microsoft-glint/Screenshots"+"test_LandingPageTitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver= setup
        time.sleep(10)
        self.driver.get(self.baseURL)
        time.sleep(10)
        self.lp=LoginPage(self.driver)
        self.lp.setEmailAddress(self.Email_address)
        self.lp.setContinuebutton1()
        time.sleep(10)
        self.lp.setCompanyId(self.Client_id)
        self.lp.setContinuebutton2()
        time.sleep(10)
        self.lp.setPassword(self.Password)
        self.lp.setContinuebutton3()
        time.sleep(10)
        actual_title=self.driver.title

        if actual_title=="Viva Glint":
            assert True
        else:
            self.driver.save_screenshot(
                "C:/Users/admin/PycharmProject/pythonProject/Microsoft-glint/Screenshots" + "test_login.png")
            self.driver.close()
            assert False

