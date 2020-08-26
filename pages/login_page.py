import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.xpathLoginButton = "//button[@data-role='loginHeaderButton']"
        self.submit = "//button[@data-id='login-button']"
        self.username = "email"
        self.password = "password"
        self.profile = "//a[@data-role='accountProfileLink']"

    def click_loginbutton(self):
        """
        This method to click on Login button
        """

        xpath = self.xpathLoginButton
        self.services.wait_for_element(xpath)
        login_button = self.driver.find_element_by_xpath(xpath)
        logging.info("# Clicking Login button")
        login_button.click()

    def enter_logindata(self):
        """
        This method to enter data into Login form
        """
        username = self.username
        password = self.password
        username = self.driver.find_element_by_name(username)
        password = self.driver.find_element_by_name(password)
        username.send_keys("betest@mailinator.com")
        password.send_keys("Betest@123")

    def login_submit(self):
        """
        This method submit Login data and check Logged In user
        """
        submit = self.submit
        profile = self.profile
        submit = self.driver.find_element_by_xpath(submit)
        submit.click()
        profile = self.driver.find_element_by_xpath(profile)
        logging.info("# Actual heading on Disappearing Elements page: %s" % profile)