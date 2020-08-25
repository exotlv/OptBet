from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# Step 1) Open Chrome
desiredCapabilities = DesiredCapabilities.CHROME.copy()
browser = webdriver.ChromeOptions()
browser.add_argument("--headless")
browser.add_argument("--no-sandbox")
browser.add_argument("--start-maximized")
browser = webdriver.Remote(options=browser, command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=desiredCapabilities)
# Step 2) Navigate to Optibet
browser.get("https://www.optibet.lt/en/login")
print(browser.title)
# Step 3) Check Login form and Enter data
browser.implicitly_wait(10)
browser.maximize_window()
element = browser.find_element_by_link_text("Forgot your password?")
username = browser.find_element_by_name("email")
password = browser.find_element_by_name("password")
submit = browser.find_element_by_xpath("//button[@data-id='login-button']")
username.send_keys("betest@mailinator.com")
password.send_keys("Betest@123")
# Step 4) Click Login and check Logged In status
submit.click()
profile = browser.find_element_by_xpath("//a[@data-role='accountProfileLink']")
browser.save_screenshot("loginRemote.png")
browser.close()
