# Author: Al3x Perotti - @cyb3rkitties

# Version 1
# Released on March 17, 2022

# Description: This script opens a new instance of CHROMEDRIVER and allows the user to authenticate. It searches among LinkedIn job postings from the past month to see how many contain the certification codes included in 'certs'. It pairs data with labels in a dictionary and exports to a CSV file. It's possible to add any other keyword or certification to the list.

# Requirements: Make sure to install a webdriver for the appropriate browser and version in use. The packages 'requests', 'bs4', and 'pandas' are also required.

# Usage: Webdriver details, "email address", and "password" need to be specified before running the script.

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# Open a new instance of webdriver

driver = webdriver.Chrome(executable_path="PATH TO WEBDRIVER") # Customize with the appropriate webdriver details

driver.get("https://linkedin.com/uas/login")
time.sleep(5)

# Authentication

username = driver.find_element_by_id("username")
username.send_keys("YOUR EMAIL ADDRESS") # CHANGE THIS
pword = driver.find_element_by_id("password")
pword.send_keys("YOUR PASSWORD") # CHANGE THIS

driver.find_element_by_xpath("//button[@type='submit']").click()

# If you have MFA enabled, this gives you time to complete that step

time.sleep(10)

certs =["CCNA", "CCNP", "ITIL", "CISSP", "MCSE", "CAP", "Sec+", "CISA", "CEH", "CISM", "CCSP", "GSEC", "CRISC", "CCIE", "OSCP", "MCSA", "SSCP", "CIPP", "CASP", "CySA+", "GICSP", "GPEN", "GCIA", "CGEIT", "CCSLP", "GCFA", "GCED", "GWAPT", "GREM", "GCFE", "OSCE", "PenTest+"] # Add certifications to this list
diz = {}

for i in certs:

    # Requesting the web page and parsing it

    webpage = requests.get(f"https://www.linkedin.com/jobs/search/?&keywords={i}&location=United%20States&sortBy=R")
    soup = BeautifulSoup(webpage.content, "html5lib")

    # Selecting the part of the page where the number of search results is stored

    for item in soup.select('label'):
        if re.search('Month', item.text):
            jobs = item.text.split()[2].replace('(','').replace(')','')

            diz[i] = jobs
            sleep(5) # Avoiding BOT triggers

# Writing data to a dataframe and exporting to a CSV file

updated_certs = pd.DataFrame.from_dict(diz, orient='index', columns=['Number of Jobs'])

updated_certs.to_csv('updated_certs.csv', index=True, index_label='Certification')
