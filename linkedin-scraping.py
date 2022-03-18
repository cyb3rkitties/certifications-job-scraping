# Author: Al3x Perotti - @cyb3rkitties

# Version 1
# Released on March 17, 2022

# Description: This script searches among LinkedIn job postings from the past month to see how many contain the certification codes included in 'certs'. It pairs data with labels in a dictionary and exports to a CSV file. It's possible to add any other keyword or certification to the list.

# Requirements: Make sure to install 'requests', 'bs4', and 'pandas' before running.

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

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
