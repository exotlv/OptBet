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
        self.logout = "//button[@data-role='logoutHeaderButton']"
        self.email_validation = "//div[@data-role='validationError'][contains(text(),'Please enter a valid email')]"
        self.password_validation = "//div[@data-role='validationError'][contains(text(),'Password is required')]"
        self.forgot = "//a[@data-role='loginForgotPasswordButton']"
        self.close = "//div[@data-role='closeIcon']"
        self.signup = "Become a member now"


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
        This method submit Login data and check Logged In user, then log out
        """
        submit = self.submit
        profile = self.profile
        submit = self.driver.find_element_by_xpath(submit)
        submit.click()
        profile = self.driver.find_element_by_xpath(profile)
        logging.info("# Actual heading on Disappearing Elements page: %s" % profile)

    def click_logoutbutton(self):
        """
        This method to click on Logout button
        """

        xpath = self.logout
        self.services.wait_for_element(xpath)
        logout_button = self.driver.find_element_by_xpath(xpath)
        logging.info("# Clicking Logout button")
        logout_button.click()

    def check_login_validation(self):
        """
        This method to check validation on Login form
        """

        username = self.username
        email_validator = self.email_validation
        username = self.driver.find_element_by_name(username)
        username.send_keys("com")
        submit = self.submit
        submit = self.driver.find_element_by_xpath(submit)
        submit.click()
        self.services.wait_for_element(email_validator)
        validation_error = self.driver.find_element_by_xpath(email_validator)
        logging.info("# Checking message: %s" % validation_error)
        username.send_keys("betest@mailinator.com")
        submit.click()
        pass_validator = self.password_validation
        self.services.wait_for_element(pass_validator)
        validation_error = self.driver.find_element_by_xpath(pass_validator)
        logging.info("# Checking message: %s" % validation_error)

    def check_elements_on_login_form(self):
        """
        This method to check different elements on Login form
        """
        forgot = self.forgot
        close = self.close
        signup = self.signup
        forgot = self.driver.find_element_by_xpath(forgot)
        close = self.driver.find_element_by_xpath(close)
        signup = self.driver.find_element_by_link_text(signup)
        logging.info("# Checking elements: %s" % forgot)
        logging.info("# Checking elements: %s" % close)
        logging.info("# Checking elements: %s" % signup)