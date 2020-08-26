from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.casino_page import CasinoPage
from utility.drivermanager import DriverManager


class SearchTest(DriverManager):
    def test_searchpage(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        casino_page = CasinoPage(self.driver)
        home_page.verify_home_page()
        casino_page.verify_casino_page()
        search_page.click_search_button()
        search_page.enter_search_data()
        search_page.validate_game_page()
