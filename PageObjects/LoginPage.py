from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    textbox_emailaddress_id="email"
    button_continue1_xpath="/html/body/glint-session-root/div/glint-session-auth/form/section/footer/button"
    textbox_companyid_id="clientUuid"
    button_continue2_xpath="/html/body/glint-session-root/div/glint-session-client/form/section/footer/button"
    textbox_password_id="password"
    button_continue3_xpath="/html/body/glint-session-root/div/glint-session-login/form/section/footer/button"

    def __init__(self,driver):
        self.driver=driver

    def setEmailAddress(self,emailaddress):
        self.driver.find_element_by_id(self.textbox_emailaddress_id).clear()
        self.driver.find_element_by_id(self.textbox_emailaddress_id).send_keys(emailaddress)

    def setContinuebutton1(self):
        self.driver.find_element_by_xpath(self.button_continue1_xpath).click()

    def setCompanyId(self,companyid):
        self.driver.find_element_by_id(self.textbox_companyid_id).clear()
        self.driver.find_element_by_id(self.textbox_companyid_id).send_keys(companyid)

    def setContinuebutton2(self):
        self.driver.find_element_by_xpath(self.button_continue2_xpath).click()

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def setContinuebutton3(self):
        self.driver.find_element_by_xpath(self.button_continue3_xpath).click()






