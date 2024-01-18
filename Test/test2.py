import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from Pages.ReportPage import ReportPage


@pytest.mark.usefixtures("setup")
class TestReportpage:

    def testexecutivesummary(self):

        exsum = ReportPage(self.driver)
        exsum.execusummary('execusummary')
        self.driver.implicitly_wait(10)

    def testheatmap(self):

        hmap = ReportPage(self.driver)
        hmap.heatmap('heatmap')
        self.driver.implicitly_wait(10)

    def testcomments(self):

        comm =ReportPage(self.driver)
        comm.comments('comments')
        self.driver.implicitly_wait(10)

    def testdriverreport(self):

        drimp = ReportPage(self.driver)
        drimp.driverimpact('driverimpact')
        self.driver.implicitly_wait(10)




