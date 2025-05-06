# testCases/test_leave_page.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.DriverFactory import DriverFactory
from utilities.CustomLogger import LogGen
from utilities.ReadConfig import ReadConfig

class Test_002_Leave:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def wait_for_element(self, by, value, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def login(self):
        self.loginPage = LoginPage(self.driver)
        self.wait_for_element(By.NAME, "username")
        self.loginPage.setUsername(self.username)
        self.wait_for_element(By.NAME, "password")
        self.loginPage.setPassword(self.password)
        self.wait_for_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        self.loginPage.clickLogin()
        WebDriverWait(self.driver, 60).until(EC.title_contains("OrangeHRM"))

    def test_navigate_to_leave_page(self):
        self.logger.info("******** Verifying Leave Page Navigation ********")
        self.driver = DriverFactory.get_driver()
        self.driver.get(self.baseURL)
        self.login()

        self.homePage = HomePage(self.driver)
        self.wait_for_element(By.XPATH, self.homePage.btn_leave_page_xpath)
        self.homePage.clickLeave()
        time.sleep(5)

        # Wait for My Leave page to load
        self.wait_for_element(By.XPATH, self.homePage.txt_myleave_header_xpath)
        self.homePage.clickLeaveHeader()
        time.sleep(5)
        my_leave_text = self.homePage.getMyLeaveHeader().text

        if my_leave_text == "My Leave":
            self.logger.info("******** My Leave Page Loaded Successfully ********")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_leave_page_failed.png")
            self.logger.error("******** My Leave Page Not Loaded ********")
            assert False

        self.driver.quit()
