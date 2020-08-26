import logging
from utility.services import Services


class CasinoPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.title = "Exclusive Casino Games - Best online casino | Optibet"
        self.casino = "//a[@data-role='Casino']"

    def verify_casino_page(self):
        """
        This method is to verify Casino page.
        return: instance of Casino page
        rtype: CasinoPage instance
        """
        casino = self.casino
        self.services.wait_for_element(casino)
        casino_button = self.driver.find_element_by_xpath(casino)
        logging.info("# Clicking Casino button")
        casino_button.click()
        logging.info('## Verifying Casino page ##')
        actual_title = self.title
        logging.info('# Actual Title: %s' % actual_title)
        assert actual_title == self.title, "Actual title %s, should be same as %s" % (actual_title, self.title)
        return self
