from selenium import webdriver
# Step 1) Open Chrome
browser = webdriver.Chrome()
# Step 2) Navigate to Optibet
browser.get("https://www.optibet.lt/en/login")
print(browser.title)
# Step 3) Search & Enter the Email or Phone field & Enter Password
browser.implicitly_wait(5)
login_window  = browser.find_element_by_link_text("Forgot your password?")
username = browser.find_element_by_name("email")
password = browser.find_element_by_name("password")
submit = browser.find_element_by_xpath("//button[@data-id='login-button']")
username.send_keys("betest@mailinator.com")
password.send_keys("Betest@123")
# Step 4) Click Login
submit.click()
profile = browser.find_element_by_xpath("//a[@data-role='accountProfileLink']")
browser.save_screenshot("login.png")
browser.close()
