from selenium.webdriver.common.by import By

class ReportPage:
    def __init__(self,driver):
        self.driver = driver

    executive_summary_report_button_xpath='//*[@id="mainContent"]/glint-report-landing/glint-reports/glint-panel/div/div/div/div[2]/div/glint-report-tile-list/ul/li[1]/button'
    heatmap_report_button_xpath='//*[@id="mainContent"]/glint-report-landing/glint-reports/glint-panel/div/div/div/div[2]/div/glint-report-tile-list/ul/li[2]/button'
    overallresults_button_xpath='//*[@id="mainContent"]/glint-report-landing/glint-reports/glint-panel/div/div/div/div[2]/div/glint-report-tile-list/ul/li[4]/button'
    commentsreport_button_xpath='/html/body/glint-root/div/div/main/glint-report-landing/glint-reports/glint-panel/div/div/div/div[2]/div/glint-report-tile-list/ul/li[4]/button'
    driverimpact_button_xpath = '//*[@id="mainContent"]/glint-report-landing/glint-reports/glint-panel/div/div/div/div[2]/div/glint-report-tile-list/ul/li[3]/button'

    def execusummary(self,execusummary):
        self.driver.find_element(By.XPATH,self.executive_summary_report_button_xpath).click()

    def heatmap(self,heatmap):
        self.driver.find_element(By.XPATH,self.heatmap_report_button_xpath).click()

    def overallresults(self,overallresults):
        self.driver.find_element(By.XPATH,self.overallresults_button_xpath).click()

    def comments(self,comments):
        self.driver.find_element(By.XPATH,self.commentsreport_button_xpath).click()

    def driverimpact(self,driverimpact):
        self.driver.find_element(By.XPATH,self.driverimpact_button_xpath).click()






