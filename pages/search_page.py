import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.search_field = "//input[@data-role='searchInput']"
        self.search_button = "search"
        self.search_data = "Dragon Stone"
        self.game_thumb = "//div[@data-role='gameThumb']"
        self.game_title = "Dragon Stone - Play Now! Best Online Casino | Optibet"

    def click_search_button(self):
        """
        This method to click on search button
        """
        button = self.search_button
        self.services.wait_for_element_name(button)
        click_button = self.driver.find_element_by_name(button)
        logging.info("# Clicking Search button")
        click_button.click()

    def enter_search_data(self):
        """
        This method to enter search data and verify
        """
        field = self.search_field
        data = self.search_data
        thumb = self.game_thumb
        self.services.wait_for_element(field)
        enter_data = self.driver.find_element_by_xpath(field)
        enter_data.send_keys(data)
        self.services.wait_for_element(thumb)

    def validate_game_page(self):
        """
        This method to validate game page after search
        """
        thumb = self.game_thumb
        self.services.wait_for_element(thumb)
        click_game = self.driver.find_element_by_xpath(thumb)
        click_game.click()
        logging.info('## Verifying game page ##')
        gametitle = self.game_title
        logging.info('# Actual Title: %s' % gametitle)
        assert gametitle == self.driver.title, "Actual title %s, should be same as %s" % (gametitle, self.driver.title)
        return self