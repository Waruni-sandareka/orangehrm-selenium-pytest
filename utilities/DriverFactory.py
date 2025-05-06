from selenium import webdriver

class DriverFactory:

    @staticmethod
    def get_driver(browser_name="chrome"):
        if browser_name == "chrome":
            driver = webdriver.Chrome()
        elif browser_name == "firefox":
            driver = webdriver.Firefox()
        else:
            raise Exception(f"Browser {browser_name} is not supported.")

        driver.maximize_window()
        return driver
