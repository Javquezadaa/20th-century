
# 20th Century Wikipedia Scraping Project

## 1. Problem Summary
When trying to use Selenium with ChromeDriver, multiple errors occurred:

- **`SessionNotCreatedException`**: ChromeDriver version mismatch with Chrome browser.
- **`NoSuchDriverException` / `ValueError`**: Incorrect path to `chromedriver`.
- ChromeDriver was not executable or located in the expected folder.
- Attempting to use `webdriver_manager` failed because the exact driver version was not available online yet.

## 2. How We Solved It
1. Verified Chrome version: `Google Chrome 139.0.7258.139`.
2. Downloaded **matching ChromeDriver version** from [official ChromeDriver site](https://chromedriver.chromium.org/downloads).
   
3. Unzipped the driver and set it executable with:
 ```bash
   chmod +x chromedriver
 ```  

4.	Verified ChromeDriver works:
```bash 
./chromedriver
```
- **Expected Output:**  
  When running `check_chrome_ready.py`, the output should show:  
- **Environment Updates:**  
1. Updated Python environment and Selenium to the latest version compatible with ChromeDriver.  
2. Specified the absolute path to ChromeDriver in the script to avoid path issues.

# 3. How to Replicate This Project

1.	Activate your environment:
 ```bash 
 conda activate 20th_century 
 ``` 
2.	Open JupyterLab or VS Code in that environment.
3.	Ensure your Chrome version matches the ChromeDriver version.
4.	Download ChromeDriver matching your Chrome version.
5.	Make it executable:
```bash 
chmod +x /path/to/chromedriver
```
6.	Keep the path consistent and point your script to it.
7.	Run the Python script to scrape the page.
8.	Save results (.txt or .csv) for future reference.

# 4. How to Check Everything is Ready

Create a file `check_chrome_ready.py` with the following content:

```python
# Import necessary Selenium modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome without opening a window (optional)
chrome_options.add_argument("--no-sandbox") # Required in some environments

# Specify the path to your chromedriver executable
chromedriver_path = "/absolute/path/to/chromedriver"
service = Service(chromedriver_path)

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a test page
driver.get("https://www.google.com")

# Print Chrome version and page title to verify everything is working
print("Chrome version:", driver.capabilities['browserVersion'])
print("Test page title:", driver.title)

# Close the browser
driver.quit()
```

Run it using:

```bash 
python check_chrome_ready.py
```
If you see the Chrome version and page title printed, everything is ready.


# 5. Final Scraping Script

Create a file `final_scraping.py` with the following content:

```python
# Importing Libraries

import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os


# Setup Chrome Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


# Setting ChromeDriver Path

chromedriver_path = "/absolute/path/to/chromedriver"  # Update path
service = Service(chromedriver_path)


# Launching WebDriver

driver = webdriver.Chrome(service=service, options=chrome_options)


# Opening Wikipedia Page

url = "https://en.wikipedia.org/wiki/Key_events_of_the_20th_century"
driver.get(url)
time.sleep(3)  # Give time for page to load


# Getting page HTML

html = driver.page_source


# Parse with BeautifulSoup

soup = BeautifulSoup(html, "html.parser")


# Extracting Text Content

page_text = soup.get_text(separator="\n")  # Get full text


# Saving to .txt file

output_path = "20th_century_events.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(page_text)

print(f"Scraping complete! Saved to {output_path}")


# Closing Chrome

driver.quit()

```


**What Each Part Does:**

- **Libraries:**  
  - `selenium` controls the browser.  
  - `BeautifulSoup` parses HTML.  
  - `pandas` is optional if you want to work with structured data.  

- **Chrome Options:**  
  - Run Chrome headless (no GUI) for faster scraping.  
  - Includes `--no-sandbox` and `--disable-dev-shm-usage` for compatibility in some environments.  

- **Service Path:**  
  - Ensures Selenium knows the exact location of `chromedriver`.  

- **WebDriver:**  
  - Opens Chrome and loads the Wikipedia page.  

- **BeautifulSoup:**  
  - Extracts text from the loaded HTML.  

- **Output:**  
  - Saves page content to `20th_century_events.txt`.  

- **Quit Driver:**  
  - Closes the browser properly to free system resources.  



# Project Workflow Flowchart

```mermaid
flowchart TD
    A[Start Project] --> B[Activate 20th_century Environment]
    B --> C[Check Chrome and ChromeDriver Versions]
    C --> D[Download & Setup ChromeDriver]
    D --> E[Run check_chrome_ready.py]
    E --> F[Open Wikipedia Page with Selenium]
    F --> G[Scrape Page Source]
    G --> H[Parse with BeautifulSoup]
    H --> I[Extract Text Content]
    I --> J[Save to .txt File]
    J --> K[Close Browser & Finish]

# ✅ Notes for Future Runs

1. Always check the Chrome version before starting.  
2. Keep the ChromeDriver version in sync with Chrome.  
3. Update Selenium if needed.  
4. Always use absolute paths for ChromeDriver.  
5. For automation, scripts can be reused by changing the `url` and `output_path`.

