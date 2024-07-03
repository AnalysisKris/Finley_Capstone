from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''

    # Setting up Chrome options
    options = Options()
    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')
    
    # Change the path to where chromedriver is in your home folder.
    service = Service(path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1120, 1000)
    
    url = f"https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword={keyword}&sc.keyword={keyword}&locT=&locId=&jobType="
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  # If true, should still be looking for new jobs.

        time.sleep(slp_time)

        # Test for the "Sign Up" prompt and get rid of it.
        try:
            driver.find_element(By.XPATH, './/button[text()="Sign Up"]').click()
        except ElementClickInterceptedException:
            pass

        time.sleep(.1)

        try:
            driver.find_element(By.XPATH, './/span[text()="Close"]').click()  # Clicking to close the pop-up.
            print(' X out worked')
        except NoSuchElementException:
            print(' X out failed')
            pass

        # Going through each job on the page
        job_buttons = driver.find_elements(By.XPATH, '/html/body/div[3]/div[1]/div[4]/div[2]/div[2]/div/div[1]/section/div[2]/div[1]')  # Job listings on the page.
        for job_button in job_buttons:

            print(f"Progress: {len(jobs)}/{num_jobs}")
            if len(jobs) >= num_jobs:
                break

            job_button.click()
            time.sleep(1)
            collected_successfully = False

            while not collected_successfully:
                try:
                    company_name = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[4]/div[2]/div[2]/div/div[1]/section/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text
                    location = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[4]/div[2]/div[2]/div/div[1]/section/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span').text
                    job_title = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[4]/div[2]/div[2]/div/div[1]/section/div[2]/div[1]/div[1]/div[1]/div[1]/a').text
                    job_description = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[4]/div[2]/div[2]/div/div[1]/section/div[2]/div[1]/div[1]/div[1]/div[2]').text
                    collected_successfully = True
                except:
                    time.sleep(5)

            try:
                salary_estimate = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[4]/div[2]/div[2]/div/div[1]/section/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/span').text
            except NoSuchElementException:
                salary_estimate = -1  # Set a default value if salary is not found.

            try:
                rating = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[4]/div[2]/div[2]/div/div[1]/section/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/span').text
            except NoSuchElementException:
                rating = -1  # Set a default value if rating is not found.

            # Printing for debugging
            if verbose:
                print(f"Job Title: {job_title}")
                print(f"Salary Estimate: {salary_estimate}")
                print(f"Job Description: {job_description[:500]}")
                print(f"Rating: {rating}")
                print(f"Company Name: {company_name}")
                print(f"Location: {location}")

            # Going to the Company tab...
            try:
                driver.find_element(By.XPATH, './/div[@class="tab" and @data-tab-type="overview"]').click()

                try:
                    headquarters = driver.find_element(By.XPATH, './/div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
                except NoSuchElementException:
                    headquarters = -1

                # Additional scraping logic for company details...

            except NoSuchElementException:  # Rarely, some job postings do not have the "Company" tab.
                headquarters = -1
                # Handle other company details...

            if verbose:
                print(f"Headquarters: {headquarters}")
                # Print other company details...

            jobs.append({
                "Job Title": job_title,
                "Salary Estimate": salary_estimate,
                "Job Description": job_description,
                "Rating": rating,
                "Company Name": company_name,
                "Location": location,
                "Headquarters": headquarters,
                # Add other fields to the dictionary
            })

        # Clicking on the "next page" button
        try:
            driver.find_element(By.XPATH, './/li[@class="next"]').click()
        except NoSuchElementException:
            print(f"Scraping terminated before reaching target number of jobs. Needed {num_jobs}, got {len(jobs)}.")
            break

    driver.quit()  # Quit the driver at the end of scraping
    return pd.DataFrame(jobs)  # This line converts the dictionary object into a pandas DataFrame.
