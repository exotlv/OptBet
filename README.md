# Python + Selenium

# Run tests
python login.py

python search.py

# Run Docker container + remote Test:
docker-compose -f docker/docker-compose-selenium.yml up

To configure remote session,
Edit /utility/drivermanager.py to Remote

//
desired_cap = {
'browserName': 'chrome',
}
self.driver = webdriver.Remote(command_executor='https://127.0.0.1:4444/wd/hub',
desired_capabilities=desired_cap)
//

## All tests will be doing a screenshot after it's done