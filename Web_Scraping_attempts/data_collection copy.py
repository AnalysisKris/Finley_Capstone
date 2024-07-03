# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:47:44 2020

@author: Ken
"""

import pandas as pd
import Web_Scraping_attempts.glassdoor_scraper as gs  # assuming you have a custom module for scraping


path= "/usr/local/chromedriver/"
#path="/opt/anaconda3/lib/python3.11/site-packages/requests/exceptions.py"

# Adjust slp_time as needed
df = gs.get_jobs('data scientist', 1000, False, path, 15)  

df.to_csv('glassdoor_jobs.csv', index=False)
