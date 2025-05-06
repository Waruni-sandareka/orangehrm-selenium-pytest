from selenium.webdriver.common.by import By


class HomePage:
    text_dashboard_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6'
    btn_leave_page_xpath = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a'
    txt_myleave_header_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a'
    dropdown_profile_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/i'
    btn_logout_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a'


    def __init__(self, driver):
        self.driver = driver

    def clickLeave(self):
        self.driver.find_element(By.XPATH, self.btn_leave_page_xpath).click()

    def getMyLeaveHeader(self):
        return self.driver.find_element(By.XPATH, self.txt_myleave_header_xpath)

    def openProfileDropdown(self):
        self.driver.find_element(By.XPATH, self.dropdown_profile_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()

    def clickLeaveHeader(self):
        self.driver.find_element(By.XPATH,self.txt_myleave_header_xpath).click()

