import logging
import unittest

from selenium import webdriver

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)
import sys, os


class DriverManager(unittest.TestCase):
    """
    This class is for instantiating web driver instances.
    """

    def setUp(self):
        """
        This method is to instantiate the web driver instance.
        """
        logging.info("## SETUP METHOD ##")
        logging.info("# Initializing the webdriver.")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get("https://www.optibet.lt/en/")

    def tearDown(self):
        """
        This is teardown method.
        It is to capture the screenshots for failed test cases,
        & to remove web driver object.
        """
        logging.info("## TEARDOWN METHOD ##")

        if sys.exc_info()[0]:
            logging.info("# Taking screenshot.")
            test_method_name = self._testMethodName
            self.driver.save_screenshot("./../screenshots/%s.png" % test_method_name)

        if self.driver is not None:
            logging.info("# Removing the webdriver.")
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()
