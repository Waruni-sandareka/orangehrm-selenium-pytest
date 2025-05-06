import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities.CustomLogger import LogGen
from utilities.DriverFactory import DriverFactory
from utilities.ReadConfig import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def wait_for_element(self, by, value, timeout=30):
        """Wait for an element to be visible"""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def wait_for_element_clickable(self, by, value, timeout=30):
        """Wait for an element to be clickable"""
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def login(self):
        """Reusable login method"""
        self.loginPage = LoginPage(self.driver)
        self.wait_for_element(By.NAME, "username")
        self.loginPage.setUsername(self.username)

        self.wait_for_element(By.NAME, "password")
        self.loginPage.setPassword(self.password)

        self.wait_for_element_clickable(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        self.loginPage.clickLogin()

        # Wait for the page to load after login
        WebDriverWait(self.driver, 60).until(
            EC.title_contains("OrangeHRM")
        )

    def test_homePageTitle(self):
        self.logger.info("******** Test_001_Login ********")
        self.logger.info("******** Verifying Home Page Title ********")
        self.driver = DriverFactory.get_driver()
        self.driver.get(self.baseURL)

        # Adding WebDriverWait to wait for the page to load completely
        WebDriverWait(self.driver, 60).until(
            EC.title_contains("OrangeHRM")  # Waiting for "OrangeHRM" to appear in the title
        )

        actual_title = self.driver.title
        expected_title = "OrangeHRM"

        if actual_title == expected_title:
            assert True
            self.logger.info("******** Home Page Title Passed ********")
            time.sleep(10)
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homePageTitle.png")
            self.logger.error("******** Home Page Title Failed ********")
            assert False

        self.driver.quit()

    def test_login(self):
        self.logger.info("******** Verifying Login Test ********")
        self.driver = DriverFactory.get_driver()
        self.driver.get(self.baseURL)

        # Reuse login method
        self.login()

        # Verify if the Dashboard text is visible
        try:
            self.wait_for_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6', timeout=30)
            self.logger.info("******** Dashboard Text is Visible ********")

            # Simulate a wait for the relevant screen to load
            time.sleep(5)
            assert True
        except Exception as e:
            self.driver.save_screenshot("./Screenshots/" + "test_login_dashboard_visibility.png")
            self.logger.error(f"******** Dashboard Text Visibility Failed: {e} ********")
            assert False

        self.driver.quit()
