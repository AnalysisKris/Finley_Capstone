from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
from bs4 import BeautifulSoup
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-minimized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the Chrome driver
chromedriver_path = '/opt/homebrew/bin/chromedriver'  # Modify this path
service = Service(chromedriver_path)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Initialize DataFrame
job_dataset = pd.DataFrame(columns=["Job Title", "Company", "Location", "Description"])

# LinkedIn job search URL
search_query = "data scientist"
location = "United States"
url = f"https://www.linkedin.com/jobs/search/?keywords={search_query}&location={location}"

try:
    driver.get(url)

    # Wait until job cards are loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "job-search-card")))

    # Scroll to the bottom of the page to load all job listings
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Parse the page source using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_cards = soup.find_all('div', class_='job-search-card')

    for job_card in job_cards:
        try:
            job_title_elem = job_card.find('h3', class_='job-title')
            job_title = job_title_elem.get_text(strip=True) if job_title_elem else ""

            company_elem = job_card.find('h4', class_='company-name')
            company = company_elem.get_text(strip=True) if company_elem else ""

            location_elem = job_card.find('span', class_='job-location')
            location = location_elem.get_text(strip=True) if location_elem else ""

            job_link = job_card.find('a', class_='job-link')['href']

            # Navigate to the job description page
            driver.get(job_link)
            time.sleep(2)

            # Wait for job description to load
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "description")))

            job_desc_soup = BeautifulSoup(driver.page_source, 'html.parser')
            job_description_elem = job_desc_soup.find('div', class_='description')
            job_description = job_description_elem.get_text(strip=True) if job_description_elem else ""

            # Append data to DataFrame
            job_dataset = job_dataset.append({
                "Job Title": job_title,
                "Company": company,
                "Location": location,
                "Description": job_description
            }, ignore_index=True)

        except Exception as e:
            print(f"Error parsing job card: {e}")

finally:
    driver.quit()

# Save the DataFrame to a CSV file
job_dataset.to_csv("data_science_jobs_linkedin.csv", index=False)
