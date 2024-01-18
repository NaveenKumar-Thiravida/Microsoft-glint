import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time

op = ChromeOptions()
op.add_experimental_option("detach", True)

@pytest.fixture()
def setup(request):
        #global driver
        driver = webdriver.Chrome(options=op)
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://app.vgqa.glint.cloud-dev.microsoft/session/auth")
        driver.implicitly_wait(10)
        search = driver.find_element(By.XPATH, '//*[@id="email"]')
        search.send_keys('qatester@glintinc.com')
        search.submit()
        driver.implicitly_wait(10)
        search = driver.find_element(By.XPATH, '//*[@id="clientUuid"]')
        search.send_keys('qa20191108')
        search.submit()
        driver.implicitly_wait(10)
        search = driver.find_element(By.XPATH, '//*[@id="password"]')
        search.send_keys('Dem0@pass2')
        search.submit()
        time.sleep(10)
        search = driver.find_element(By.XPATH, '//*[@id="tab-4"]')
        search.click()
        time.sleep(5)
        request.cls.driver = driver
        yield
        driver.quit()