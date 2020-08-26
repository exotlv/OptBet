import logging
from utility.services import Services
from pages.login_page import LoginPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.title = "Optibet: Best Online Casino, Sports betting, Live betting"

    def verify_home_page(self):
        """
        This method is to verify Home page.
        return: instance of Home page
        rtype: HomePage instance
        """

        logging.info('## Verifying home page ##')
        actual_title = self.title
        logging.info('# Actual Title: %s' % actual_title)
        assert actual_title == self.title, "Actual title %s, should be same as %s" % (actual_title, self.title)
        return self

    def click_on_link(self, link_txt):
        """
        This method is to click on the Login link at the Home page.

        param link_txt: link text present on the Home page
        type link_txt: string
        """

        logging.info("# Click on link '%s'" % link_txt)

        # Link Text: Login button
        if link_txt == "Login":
            login_page = LoginPage(self.driver)
            login_page.click_loginbutton()
            return login_page
