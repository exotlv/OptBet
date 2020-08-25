# Python + Selenium

# Run tests
python Login.py
python Search.py

# Run Docker container + remote Test:
docker-compose -f docker/docker-compose-selenium.yml up
python LoginRemote.py

## All tests will be doing a screenshot after it's done