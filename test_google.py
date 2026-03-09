from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start browser
driver = webdriver.Chrome(options=options)

# Open Google
driver.get("https://www.google.com")

print("Google opened successfully")

# Close browser
driver.quit()
