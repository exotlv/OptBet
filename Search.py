from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# Step 1) Open Chrome
desiredCapabilities = DesiredCapabilities.CHROME.copy()
browser = webdriver.ChromeOptions()
# browser.add_argument("--headless")
browser.add_argument("--no-sandbox")
browser.add_argument("--start-maximized")
browser = webdriver.Chrome(options=browser, desired_capabilities=desiredCapabilities)
# browser.add_argument("--start-maximized")
# Step 2) Navigate to Optibet
browser.get("https://www.optibet.lt/en/casino/exclusive_casino_games?filter=all")
print(browser.title)
# Step 3) Open Search form and type game name there
browser.implicitly_wait(5)
search  = browser.find_element_by_name("search").click()
search_field = browser.find_element_by_xpath("//input[@data-role='searchInput']")
search_field.send_keys("Dragon Stone")
# Step 4) Check found game and click on it
game_thumb = browser.find_element_by_xpath("//div[@data-role='gameThumb']").click()
# Step 5) Check that correct Game page is opened
print(browser.title)
if not "Dragon Stone" in browser.title:
    raise Exception("Game page is not Dragon Stone")
browser.save_screenshot("search.png")
browser.close()

