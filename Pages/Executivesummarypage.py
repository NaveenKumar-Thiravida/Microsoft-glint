from selenium.webdriver.common.by import By


class Executivesummarypage:
    def __init__(self, driver):
        self.driver = driver

    executive_summary_report_button_xpath = '//*[@id="mainContent"]/glint-report-landing/glint-reports/glint-panel/div/div/div/div[2]/div/glint-report-tile-list/ul/li[1]/button'
    pulse_change_button_xpath = '//*[@id="filterPanelMain"]/div[2]/div/div[1]/glint-reported-survey-list/glint-reported-survey/div/div[2]/div[1]/div/glint-survey-range-picker/glint-pulse-range-picker/glint-dropdown/div/div'
    click_pulse_month = '//*[@id="filterPanelMain"]/div[1]/div/div[1]/glint-reported-survey-list/glint-reported-survey/div/div[2]/div[1]/div/glint-survey-range-picker/glint-pulse-range-picker/glint-dropdown/div/div'
    select_november_pulse = '//*[@id="option2"]'
    x_button = '/html/body/glint-root/div/div/main/glint-engagement-report/glint-report-detail/section[1]/glint-survey-report-panel/glint-report-panel/div[1]/div/div[2]/div/div[2]/button'
    settings_button = '//*[@id="reportEditButton"]'
    show_dropdown = '/html/body/glint-root/div/div/main/glint-engagement-report/glint-report-detail/glint-report-section-edit-slidey/glint-slidey/div/div[3]/div/div/section/div/glint-report-section-form/form/div[2]/glint-dropdown/div/div/div'
    companyupdated_button = '/html/body/glint-root/div/div/main/glint-engagement-report/glint-report-detail/glint-report-section-edit-slidey/glint-slidey/div/div[3]/div/div/section/div/glint-report-section-form/form/div[2]/glint-dropdown/div/div/div[2]/ul/li[4]'
    done_button = '/html/body/glint-root/div/div/main/glint-engagement-report/glint-report-detail/glint-report-section-edit-slidey/glint-slidey/div/div[3]/div/header/div/div/div/button'


    def execsummary(self, execsummary):
        self.driver.find_element(By.XPATH, self.executive_summary_report_button_xpath).click()

    def changepulse(self, changepulse):
        self.driver.find_element(By.XPATH, self.pulse_change_button_xpath).click()

    def clickmonth(self, clickmonth):
        self.driver.find_element(By.XPATH, self.click_pulse_month).click()

    def setnov(self, setnov):
        self.driver.find_element(By.XPATH, self.select_november_pulse).click()

    def x(self, x):
        self.driver.find_element(By.XPATH, self.x_button).click()

    def settings(self, settings):
        self.driver.find_element(By.XPATH, self.settings_button).click()

    def show(self, show):
        self.driver.find_element(By.XPATH, self.show_dropdown).click()

    def company(self, company):
        self.driver.find_element(By.XPATH, self.companyupdated_button).click()

    def done(self,done):
        self.driver.find_element(By.XPATH, self.done_button).click()
