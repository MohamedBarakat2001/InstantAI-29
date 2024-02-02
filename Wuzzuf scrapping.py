#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[5]:


website = "https://wuzzuf.net/search/jobs/?q=AI+Engineer&a=hpb"
website_html = requests.get(website)
website_html


# In[9]:


soup = BeautifulSoup(website_html.content , 'lxml')
soup


# In[19]:


jobs = soup.find_all("div" , class_="css-pkv5jc")

for job in jobs:
    job_title = job.find("a" , class_="css-o171kl").text
    address = job.find("span" , class_="css-5wys0k").text
    company_name= job.find("a" , class_="css-17s97q8").text
    job_type = job.find("span" , class_="css-1ve4b75 eoyjyou0").text
    print(job_title,address,company_name,job_type)
    



# In[22]:


import csv


# In[23]:


csvfile = open ('AIRound29jobs.csv', 'w', encoding='utf-8') # w = write into the file , general way of representing data 
writer = csv.writer(csvfile)


# In[ ]:





# In[24]:


writer.writerow(['Job title', 'Company', 'location', 'job type'])


# In[25]:


jobs = soup.find_all("div" , class_="css-pkv5jc")

for job in jobs:
    job_title = job.find("a" , class_="css-o171kl").text
    address = job.find("span" , class_="css-5wys0k").text
    company_name= job.find("a" , class_="css-17s97q8").text
    job_type = job.find("span" , class_="css-1ve4b75 eoyjyou0").text
    
    writer.writerow([job_title, address, company_name,job_type])
csvfile.close()
    


# In[ ]:




