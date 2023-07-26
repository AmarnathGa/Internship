#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings


# In[3]:


warnings.filterwarnings("ignore")

import time


# # 1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You 
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 
# jobs data.

# In[6]:


driver = webdriver.Chrome()


# In[7]:


driver.get("https://www.naukri.com/")


# In[8]:


designation=driver.find_element(By.CLASS_NAME, "suggestor-input")
designation.send_keys('Data Analyst')


# In[9]:


Location=driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
Location.send_keys('Banglore')


# In[10]:


Search=driver.find_element(By.CLASS_NAME, "qsbSubmit")
Search.click()


# In[11]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[12]:


title_tag=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tag[0:10]:
    title=i.text
    job_title.append(title)


# In[13]:


location_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tag[0:10]:
    location=i.text
    job_location.append(location)


# In[14]:


company_tag=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    company=i.text
    company_name.append(company)


# In[15]:


experience_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tag[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[17]:


import pandas as pd
df=pd.DataFrame({'Title':job_title, 'location':job_location,'Company':company_name, 'Experience':experience_required})
df


# # Q2 Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You 
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.

# In[18]:


driver = webdriver.Chrome()


# In[19]:


driver.get("https://www.naukri.com/")


# In[20]:


designation=driver.find_element(By.CLASS_NAME, "suggestor-input")
designation.send_keys('Data Scientist')


# In[21]:


Location=driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
Location.send_keys('Banglore')


# In[22]:


Search=driver.find_element(By.CLASS_NAME, "qsbSubmit")
Search.click()


# In[23]:


job_title2=[]
job_location2=[]
company_name2=[]
experience_required2=[]


# In[24]:


title_tag=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tag[0:10]:
    title=i.text
    job_title2.append(title)


# In[26]:


location_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tag[0:10]:
    location=i.text
    job_location2.append(location)


# In[27]:


company_tag=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    company=i.text
    company_name2.append(company)


# In[28]:


experience_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tag[0:10]:
    experience=i.text
    experience_required2.append(experience)


# In[29]:


import pandas as pd
df=pd.DataFrame({'Title':job_title2, 'location':job_location2,'Company':company_name2, 'Experience':experience_required2})
df


# # Q3: In this question you have to scrape data using the filters available on the webpage as shown below
#     you have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required. 
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs

# In[30]:


driver = webdriver.Chrome()


# In[31]:


driver.get("https://www.naukri.com/")


# In[32]:


designation=driver.find_element(By.CLASS_NAME, "suggestor-input")
designation.send_keys('Data Scientist')


# In[33]:


Location=driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
Location.send_keys('Delhi/NCR')


# In[34]:


Search=driver.find_element(By.CLASS_NAME, "qsbSubmit")
Search.click()


# In[35]:


Salary=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]")
Salary.click()


# In[36]:


job_title3=[]
job_location3=[]
company_name3=[]
experience_required3=[]


# In[37]:


title_tag=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tag[0:10]:
    title=i.text
    job_title3.append(title)


# In[38]:


location_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tag[0:10]:
    location=i.text
    job_location3.append(location)


# In[39]:


company_tag=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    company=i.text
    company_name3.append(company)


# In[40]:


experience_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tag[0:10]:
    experience=i.text
    experience_required3.append(experience)


# In[41]:


import pandas as pd
df=pd.DataFrame({'Title':job_title3, 'location':job_location3,'Company':company_name3, 'Experience':experience_required3})
df


# # Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. ProductDescription
# 3. Price
# The attributes which you have to scrape is ticked marked in the below image.

# In[42]:


driver = webdriver.Chrome()


# In[43]:


driver.get("https://www.flipkart.com/")


# In[44]:


product=driver.find_element(By.CLASS_NAME, "Pke_EE")
product.send_keys('sunglasses')


# In[45]:


Search=driver.find_element(By.CLASS_NAME, "_2iLD__")
Search.click()


# In[55]:


Brand0=[]
ProductDescription1=[]
Price=[]


# In[56]:


start=0
end=3
for page in range(start,end):
    Brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in Brand[0:100]:
        Brand0.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)
    


# In[58]:


len(Brand0)start=0
end=3
for page in range(start,end):
    Brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in Brand[0:100]:
        Brand0.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[59]:


start=0
end=3
for page in range(start,end):
    disc=driver.find_elements(By.XPATH,'//a[@class="_3bPFwb"]')
    for i in disc[0:100]:
        ProductDescription1.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[61]:


len(ProductDescription1)


# In[62]:


start=0
end=3
for page in range(start,end):
    p=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in p[0:100]:
        Price.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[63]:


len(Price)


# In[8]:


import pandas as pd
df=pd.DataFrame({'Brand':Brand0, 'Discription':ProductDescription1,'Price':Price})
df


# # Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market
# place=FLIPKAR

# In[7]:


driver = webdriver.Chrome()


# In[9]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market")


# In[10]:


Review=[]


# In[11]:


start=0
end=10
for page in range(start,end):
    R=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in R[0:100]:
        Review.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(11)


# In[13]:


len(Review)


# In[14]:


import pandas as pd
df=pd.DataFrame({'Review':Review})
df


# # Q6: Scrape data forfirst 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the 
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price

# In[15]:


driver = webdriver.Chrome()


# In[16]:


driver.get("https://www.flipkart.com/")


# In[19]:


product=driver.find_element(By.CLASS_NAME, "_3704LK")
product.send_keys('Sneakers')


# In[20]:


Search=driver.find_element(By.CLASS_NAME, "L0Z3Pu")
Search.click()


# In[21]:


Brand2=[]
ProductDescription2=[]
Price2=[]


# In[22]:


start=0
end=3
for page in range(start,end):
    Brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in Brand[0:100]:
        Brand2.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[23]:


start=0
end=3
for page in range(start,end):
    p=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in p[0:100]:
        Price2.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[24]:


start=0
end=3
for page in range(start,end):
    disc=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in disc[0:100]:
        ProductDescription2.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[29]:


import pandas as pd
df=pd.DataFrame({'Brand':Brand2, 'price':Price2})
df


# # Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then 
# set CPU Type filter to “Intel Core i7” as shown in the below image:

# In[32]:


driver = webdriver.Chrome()


# In[33]:


driver.get("https://www.amazon.in/")


# In[38]:


Product=driver.find_element(By.XPATH, '//input[@class="nav-input nav-progressive-attribute"]')
Product.send_keys('Laptop')


# In[40]:


Search=driver.find_element(By.XPATH, '//div[@class="nav-search-submit nav-sprite"]')
Search.click()


# In[41]:


Range=driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[7]/span[10]/li/span/a/span")
Range.click()


# In[43]:


Tittle7=[]
Rating7=[]
Price7=[]


# In[44]:


title_tag=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title_tag[0:10]:
    title=i.text
    Tittle7.append(title)


# In[45]:


price_tag=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tag[0:10]:
    price=i.text
    Price7.append(price)


# In[46]:


R_tag=driver.find_elements(By.XPATH,'//a[@class="a-popover-trigger a-declarative"]')
for i in R_tag[0:10]:
    R=i.text
    Rating7.append(R)


# In[47]:


import pandas as pd
df=pd.DataFrame({'Title':Tittle7, 'price':Price7, 'Rating':Rating7})
df


# # Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuotes
# 3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[4]:


driver = webdriver.Chrome()


# In[5]:


driver.get("https://www.azquotes.com/")


# In[50]:


#/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a


# In[6]:


Top=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a")
Top.click()


# In[7]:


Quote=[]
Author=[]
Type_of_code=[]


# In[8]:


start=0
end=10
for page in range(start,end):
    A=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in A[0:1000]:
        Author.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a')
    next_button.click()
    time.sleep(11)


# In[11]:


len(Author)


# In[12]:


start=0
end=10
for page in range(start,end):
    T=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in T[0:1000]:
        Quote.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a')
    next_button.click()
    time.sleep(11)


# In[13]:


import pandas as pd
df=pd.DataFrame({'Author':Author, 'Quote':Quote})
df


# # Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. 
# Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpagehttps://www.motor1.com/
# 2. Then You have to type in the search bar ’50 most expensive cars’
# 3. Then click on 50 most expensive carsin the world..
# 4. Then scrap the mentioned data and make the dataframe.

# In[14]:


driver = webdriver.Chrome()


# In[15]:


driver.get("https://www.motor1.com/")


# In[16]:


Product=driver.find_element(By.XPATH, '//input[@class="m1-search-panel-input m1-search-form-text"]')
Product.send_keys('50 most expensive cars')


# In[17]:


Search=driver.find_element(By.XPATH, '//button[@class="m1-search-panel-button m1-search-form-button-animate icon-search-svg"]')
Search.click()


# In[18]:


#/html/body/div[10]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a


# In[19]:


Car=driver.find_element(By.XPATH, '/html/body/div[10]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a')
Car.click()


# In[20]:


Top_Cars=[]


# In[22]:


top=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in top[0:50]:
    top=i.text
    Top_Cars.append(top)


# In[23]:


import pandas as pd
df=pd.DataFrame({'Top 50 Cars':Top_Cars})
df


# In[ ]:




