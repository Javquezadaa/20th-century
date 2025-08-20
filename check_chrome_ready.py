import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def check_chrome_version():
    try:
        output = subprocess.check_output(
            ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"],
            stderr=subprocess.STDOUT
        )
        print("Chrome version:", output.decode().strip())
    except Exception as e:
        print("Error checking Chrome version:", e)

def check_chromedriver_version(chromedriver_path):
    try:
        output = subprocess.check_output([chromedriver_path, "--version"], stderr=subprocess.STDOUT)
        print("ChromeDriver version:", output.decode().strip())
    except Exception as e:
        print("Error checking ChromeDriver:", e)

def check_selenium():
    try:
        import selenium
        print("Selenium version:", selenium.__version__)
    except ImportError:
        print("Selenium is not installed. Install with 'pip install selenium'")

def test_selenium(chromedriver_path):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://www.google.com")
        print("Test page title:", driver.title)
        driver.quit()
    except Exception as e:
        print("Error launching Selenium:", e)

if __name__ == "__main__":
    chromedriver_path = "/Users/javieraquezada/Downloads/chromedriver"  # adjust if needed
    check_chrome_version()
    check_chromedriver_version(chromedriver_path)
    check_selenium()
    test_selenium(chromedriver_path)
