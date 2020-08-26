from pages.home_page import HomePage
from pages.login_page import LoginPage
from utility.drivermanager import DriverManager


class LoginTest(DriverManager):
    def test_login_on_homepage(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        home_page.verify_home_page().click_on_link("Login")
        login_page.enter_logindata()
        login_page.login_submit()
