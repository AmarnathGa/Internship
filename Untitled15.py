#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().system('pip install selenium')


# In[14]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings


# In[15]:


warnings.filterwarnings("ignore")

import time


# In[31]:


driver = webdriver.Chrome()


# # 1. Write a python program which searches all the product under a particular product from www.amazon.in. The
# product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for
# guitars

# In[17]:


driver.get("https://www.amazon.in/")


# In[18]:


Product=driver.find_element(By.XPATH, '//input[@class="nav-input nav-progressive-attribute"]')
Product.send_keys('Guitar')


# In[19]:


Search=driver.find_element(By.XPATH, '//div[@class="nav-search-submit nav-sprite"]')
Search.click()


# # 2. In the above question, now scrape the following details of each product listed in first 3 pages of your search
# results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then
# scrape all the products available under that product name. Details to be scraped are: "Brand
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. 

# In[10]:


Brand=[]
Product=[]
Price=[]
Return=[]
Delivery=[]
Availability=[]


# In[21]:


start=0
end=3
for page in range(start,end):
    A=driver.find_elements(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]')
    for i in A[0:1000]:
        Brand.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[64]/div/div/span/a[3]')
    next_button.click()
    time.sleep(3)


# In[25]:


start=0
end=3
for page in range(start,end):
    A=driver.find_elements(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]')
    for i in A:
        Brand.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[64]/div/div/span/a[3]')
    next_button.click()
    time.sleep(3)


# In[28]:


start=0
end=3
for page in range(start,end):
    A=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]')
    for i in A[0:1000]:
        Product.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[64]/div/div/span/a[3]')
    next_button.click()
    time.sleep(3)


# In[29]:


start=0
end=3
for page in range(start,end):
    A=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
    for i in A[0:1000]:
        Price.append(i.text)
    next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[64]/div/div/span/a[3]")
    next_button.click()
    time.sleep(3)


# In[30]:


start=0
end=3
for page in range(start,end):
    A=driver.find_elements(By.XPATH,'//span[@class="a-color-base a-text-bold"]')
    for i in A[0:1000]:
        Delivery.append(i.text)
    next_button=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[64]/div/div/span/a[3]")
    next_button.click()
    time.sleep(3)


# # Write a python program to access the search bar and search button on images.google.com and scrape 10
# images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’

# In[32]:


driver.get("chrome://newtab/")


# In[ ]:


Image=driver.find_element(By.XPATH, '//div[@class="nav-search-submit nav-sprite"]')
Image.click()

