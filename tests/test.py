from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Specify the path to the ChromeDriver executable
chrome_driver_path = 'D:\\Python Learning\\lib\\chromedriver.exe'

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')  # Run Chrome in headless mode (optional)
# Create a ChromeDriver service
service = Service(chrome_driver_path)

# Create a ChromeDriver instance
# Create a ChromeDriver instance with the service and options
browser = webdriver.Chrome(service=service, options=chrome_options)

# Rest of your code...
browser.get('http://localhost:8000')

assert 'The install worked successfully' in browser.title, "Not found in title"