from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-minimized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the Chrome driver
chromedriver_path = '/opt/homebrew/bin/chromedriver'  # Modify this path if necessary
service = Service(chromedriver_path)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.linkedin.com/jobs/search/?currentJobId=3960253498&distance=25.0&geoId=103644278&keywords=data%20science&origin=HISTORY'

try:
    driver.get(url)

    # Wait until the job description element is visible

    # Wait until the job description element is visible
    job_desc = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='disabled ember-view job-card-container__link']"))
)

    # Get the HTML of the element and pass into BeautifulSoup parser
    soup = BeautifulSoup(job_desc.get_attribute('outerHTML'), 'html.parser')

    # Extract text content
    job_text = soup.get_text(separator='\n\n')
    print(job_text)

except TimeoutException:
    print("Timed out waiting for job description element to load")
except NoSuchElementException:
    print("Job description element not found")

finally:
    driver.quit()
