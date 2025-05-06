# testCases/test_logout.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.DriverFactory import DriverFactory
from utilities.CustomLogger import LogGen
from utilities.ReadConfig import ReadConfig

class Test_003_Logout:
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

    def test_logout(self):
        self.logger.info("******** Verifying Logout Functionality ********")
        self.driver = DriverFactory.get_driver()
        self.driver.get(self.baseURL)
        self.login()

        self.homePage = HomePage(self.driver)

        # Open user dropdown and click logout
        self.wait_for_element(By.XPATH, self.homePage.dropdown_profile_xpath)
        self.homePage.openProfileDropdown()
        time.sleep(5)

        self.wait_for_element(By.XPATH, self.homePage.btn_logout_xpath)
        self.homePage.clickLogout()
        time.sleep(2)

        # Verify return to login page
        self.wait_for_element(By.NAME, "username")
        if self.driver.current_url.endswith("/auth/login"):
            self.logger.info("******** Logout Successful ********")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_logout_failed.png")
            self.logger.error("******** Logout Failed ********")
            assert False

        self.driver.quit()
