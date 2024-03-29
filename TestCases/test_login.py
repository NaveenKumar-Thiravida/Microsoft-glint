import time
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGeneration

class Test_001_Login:

    url = ReadConfig.getApplicationURL()
    email_address = ReadConfig.getEmailAddress()
    client_id = ReadConfig.getClientID()
    password = ReadConfig.getPassword()

    logger=LogGeneration.loggen()


    def test_LandingPageTitle(self,setup):


        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Landing page Title **********")

        self.driver = setup
        self.driver.maximize_window()
        time.sleep(10)

        self.driver.get(self.url)
        time.sleep(10)
        actual_title=self.driver.title

        if actual_title=="Authenticate - Viva Glint":
            assert True
            self.driver.close()
            self.logger.info("********** Landing Page Title Test Is Passed **********")

        else:
            self.driver.save_screenshot("C:/Users/admin/PycharmProject/pythonProject/Microsoft-glint/Screenshots"
                                        +
                                        "test_LandingPageTitle.png")
            self.driver.close()
            self.logger.error("********** Landing Page Title Test Is Failed **********")
            assert False


    def test_login(self,setup):


        self.logger.info("********** Verifying Login Test **********")
        self.driver= setup
        self.driver.maximize_window()
        time.sleep(10)
        self.driver.get(self.url)
        time.sleep(10)
        self.lp=LoginPage(self.driver)
        self.lp.setEmailAddress(self.email_address)
        self.lp.setContinuebutton1()
        time.sleep(10)
        self.lp.setCompanyId(self.client_id)
        self.lp.setContinuebutton2()
        time.sleep(10)
        self.lp.setPassword(self.password)
        self.lp.setContinuebutton3()
        time.sleep(10)
        actual_title=self.driver.title

        if actual_title=="Viva Glint":
            assert True
            self.logger.info("********** Login Test Is Passed **********")
            self.driver.close()
        else:

            self.driver.save_screenshot(
                "C:/Users/admin/PycharmProject/pythonProject/Microsoft-glint/Screenshots" + "test_login.png")
            self.driver.close()
            self.logger.error("********** Login Test Is Failed **********")
            assert False
