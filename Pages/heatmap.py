from selenium.webdriver.common.by import By

class heatmap:
    def __init__(self, driver):
        self.driver = driver

    heatmap_button = '//*[@id="mainContent"]/glint-report-landing/glint-reports/glint-panel/div/div/div/div[2]/div/glint-report-tile-list/ul/li[2]/button'
    attribute1_button = '/html/body/glint-root/div/div/main/glint-engagement-report/glint-report-detail/div/section[2]/glint-report-section[1]/glint-heatmap-by-demographic/vg-section-layout/div/vg-layout-header/div/div/div/glint-demographic-header/glint-dropdown/div/div/div'
    settings_button = '//*[@id="reportEditButton"]'
    ungrouped_button = '//*[@id="section9ca16464-cd80-4905-916c-5077be9cce2b"]/vg-section-layout/div/vg-layout-header/div/div/div/div[2]/label[2]'
    more_button = '/html/body/glint-root/div/div/main/glint-engagement-report/glint-report-detail/section[2]/glint-report-header/div/div/div[1]/div/glint-report-template-tools/glint-dropdown[1]/div/div/div'
    grouped_button = '/html/body/glint-root/div/div/main/glint-engagement-report/glint-report-detail/div/section[2]/glint-report-section[1]/glint-heatmap-by-demographic/vg-section-layout/div/vg-layout-header/div/div/div/div[2]/label[1]'

    def heatmapbutton(self,heatmapbutton):
        self.driver.find_element(By.XPATH, self.heatmap_button).click()

    def attribute1(self,attribute1):
        self.driver.find_element(By.XPATH, self.attribute1_button).click()

    def settings(self,settings):
        self.driver.find_element(By.XPATH, self.settings_button).click()

    def ungrouped(self,ungrouped):
        self.driver.find_element(By.XPATH ,self.ungrouped_button).click()

    def more(self,more):
        self.driver.find_element(By.XPATH,self.more_button).click()

    def group(self,group):
        self.driver.find_element(By.XPATH,self.grouped_button).click()

