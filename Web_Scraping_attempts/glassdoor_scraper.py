from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-minimized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1120, 1000)

    try:
        # Clicking the first "selected" element (if any)
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.selected')))
        element.click()
    except NoSuchElementException:
        print("No element with class 'selected' found to click.")
    except ElementClickInterceptedException:
        print("ElementClickInterceptedException: Element couldn't be clicked.")
    except Exception as e:
        print(f"Error clicking on element: {e}")

    url = f"https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword={keyword}&sc.keyword={keyword}&locT=&locId=&jobType="
    driver.get(url)

    jobs = []

    while len(jobs) < num_jobs:
        time.sleep(slp_time)

        try:
            # Clicking the first "selected" element (if any)
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.selected')))
            element.click()
        except NoSuchElementException:
            print("No element with class 'selected' found to click.")
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: Element couldn't be clicked.")
        except Exception as e:
            print(f"Error clicking on element: {e}")

        time.sleep(.1)

        try:
            # Closing any pop-up modal
            close_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[alt="Close"]')))
            close_button.click()
            print('x out worked')
        except NoSuchElementException:
            print('x out failed')
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: Element couldn't be clicked.")
        except Exception as e:
            print(f"Error clicking close button: {e}")

        job_buttons = driver.find_elements(By.CLASS_NAME, "jl")
        for job_button in job_buttons:
            try:
                job_button.click()  # Click each job listing

                # Example: Extract job title
                try:
                    job_title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, './/div[@class="jobInfoItem jobTitle"]/span')))
                    jobs.append({"Job Title": job_title.text})
                except NoSuchElementException:
                    print("Job element not found")

                if len(jobs) >= num_jobs:
                    break
            except ElementClickInterceptedException:
                print("ElementClickInterceptedException: Element couldn't be clicked.")
            except Exception as e:
                print(f"Error clicking job button: {e}")

        try:
            # Clicking the next button to go to the next page
            next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, './/li[@class="next"]//a')))
            next_button.click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: Element couldn't be clicked.")
        except Exception as e:
            print(f"Error clicking next button: {e}")

    driver.quit()  # Close the WebDriver after scraping is complete
    return pd.DataFrame(jobs)

# Example usage
path = '/opt/homebrew/bin/chromedriver'
df = get_jobs('data scientist', 10, False, path, 5)  # Adjust number of jobs and sleep time as needed
df.to_csv('glassdoor_jobs.csv', index=False)
