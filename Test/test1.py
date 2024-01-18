import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from Pages.Executivesummarypage import Executivesummarypage


@pytest.mark.usefixtures("setup")
class TestGLINT:

    def testcase3(self):
        Execsummarypage = Executivesummarypage(self.driver)
        Execsummarypage.execsummary('execsummary')
        self.driver.implicitly_wait(10)
        Execsummarypage.changepulse('pulsechange')
        self.driver.implicitly_wait(10)
        Execsummarypage.clickmonth('clickmonth')
        self.driver.implicitly_wait(10)
        Execsummarypage.setnov('setnov')
        time.sleep(5)
        Execsummarypage.x('x')
        self.driver.implicitly_wait(10)
        Execsummarypage.settings('settings')
        self.driver.implicitly_wait(10)
        Execsummarypage.show('show')
        self.driver.implicitly_wait(10)
        Execsummarypage.company('company')
        self.driver.implicitly_wait(10)
        Execsummarypage.done('done')
        self.driver.implicitly_wait(10)
        time.sleep(5)

    def testcase4(self):

        Execsummarypage = Executivesummarypage(self.driver)
        Execsummarypage.execsummary('execsummary')
        self.driver.implicitly_wait(10)
        Execsummarypage.changepulse('pulsechange')
        self.driver.implicitly_wait(10)
        Execsummarypage.clickmonth('clickmonth')
        self.driver.implicitly_wait(10)
        Execsummarypage.setnov('setnov')
        self.driver.implicitly_wait(10)
        Execsummarypage.x('x')
        time.sleep(5)




