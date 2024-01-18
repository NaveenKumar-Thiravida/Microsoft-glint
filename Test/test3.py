import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from Pages.heatmap import heatmap


@pytest.mark.usefixtures("setup")
class TestHEATMAP:

    def testheatmapreport(self): #test whether heatmapbutton is clickable or not

        hmap = heatmap(self.driver)
        hmap.heatmapbutton('heatmapbutton')
        self.driver.implicitly_wait(10)

    def testattribute1(self): #test whether attribute1 is clickable or not

        att1= heatmap(self.driver)
        att1.heatmapbutton('heatmapbutton')
        att1.attribute1('attribute1')
        self.driver.implicitly_wait(10)

    def testsetting(self): #test whether setting button exists

        sett= heatmap(self.driver)
        sett.heatmapbutton('heatmapbutton')
        sett.settings('settings')
        self.driver.implicitly_wait(10)

    def testmore(self): #test whether more button is clickable

        moreb = heatmap(self.driver)
        moreb.heatmapbutton('heatmapbutton')
        moreb.more('more')
        self.driver.implicitly_wait(10)

    def testungrouped(self):  #test whether ungrouped and grouped is clickable

        ungroup =heatmap(self.driver)
        ungroup.heatmapbutton('heatmapbutton')
        ungroup.ungrouped('ungrouped')
        self.driver.implicitly_wait(10)
        ungroup.group('group')
        self.driver.implicitly_wait(10)
        


