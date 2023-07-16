#!/usr/bin/env python
# coding: utf-8

# # Question 1- Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# In[1]:


import re


# In[2]:


def fx(string):
    fx=re.compile(r'[^a-zA-Z0-9]')
    b=fx.search(string)
    return not bool(string)


# In[3]:


print(fx("ABCabc123"))
print(fx('*$%}{'))


# In[ ]:





# # Question 2- Create a function in python that matches a string that has an a followed by zero or more b's

# In[13]:


import re


# In[14]:


def match(text):
    pattern= '^a(b*)$'
    if re.search(pattern, text):
        return 'true'
    else:
        return 'false'


# In[16]:


print(match('ab'))
print(match('abc'))
print(match('a'))


# In[ ]:





# # Question 3-  Create a function in python that matches a string that has an a followed by one or more b's

# In[17]:


import re


# In[18]:


def match(text):
    pattern= 'ab+?'
    if re.search(pattern, text):
        return 'true'
    else:
        return 'false'


# In[19]:


print(match('ab'))
print(match('abc'))


# In[ ]:





# # Question 4- Create a function in Python and use RegEx that matches a string that has an a followed by zero or one 'b'.

# In[20]:


import re


# In[21]:


def match(text):
    pattern= 'ab?'
    if re.search(pattern, text):
        return 'true'
    else:
        return 'false'


# In[22]:


print(match('ab'))
print(match('abc'))
print(match('abbc'))
print(match('aabbc'))


# In[ ]:





# # Question 5- Write a Python program that matches a string that has an a followed by three 'b'.

# In[23]:


import re


# In[24]:


def match(text):
    pattern= 'ab{3}?'
    if re.search(pattern, text):
        return 'true'
    else:
        return 'false'


# In[25]:


print(match('abbb'))
print(match('aabbbbbc'))


# In[ ]:





# # Question 6- Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
# 

# In[26]:


import re


# In[29]:


txt = 'ImportanceOfRegularExpressionsInPython'


# In[30]:


print(re.findall('[A-Z][^A-Z]*', txt))


# In[ ]:





# # Question 7- Write a Python program that matches a string that has an a followed by two to three 'b'.

# In[4]:


import re


# In[7]:


def match(text):
    patterns = 'ab{2,3}'
    if re.search(patterns, text):
        return 'matched'
    else:
        return 'not unmatched'


# In[8]:


print(match("ab"))
print(match("aabbbbbc"))


# # Question 8- Write a Python program to find sequences of lowercase letters joined with a underscore.

# In[9]:


import re


# In[10]:


def match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns, text):
        return 'matched'
    else:
        return 'not unmatched'


# In[11]:


print(match("abc_xyz"))
print(match("jkl_abc"))
print(match("mno_pqr"))


# # Question 9- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# In[12]:


import re


# In[13]:


def match(text):
    patterns = 'a.*?b$'
    if re.search(patterns, text):
        return 'matched'
    else:
        return 'not unmatched'


# In[14]:


print(match("artughfbtdsxb"))
print(match("ahjcf1"))
print(match("aswdrtvmkuy"))


# # Question 10- Write a Python program that matches a word at the beginning of a string.

# In[15]:


import re


# In[16]:


def match(text):
    patterns = '^\w+'
    if re.search(patterns, text):
        return 'matched'
    else:
        return 'not unmatched'


# In[17]:


print(match("Language is an emaotion."))
print(match(" Language is an emaotion. "))


# # Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[18]:


import re


# In[19]:


def match(text):
    patterns = '^[a-zA-Z0-9_]*$'
    if re.search(patterns, text):
        return 'matched'
    else:
        return 'not unmatched'


# In[20]:


print(match("Language is an emaotion."))
print(match("Language_is_emotion"))


# # Question 12- Write a Python program where a string will start with a specific number. 

# In[21]:


import re


# In[29]:


def num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return 'True'
    else:
        return 'false'


# In[31]:


print(num('51-123456'))
print(num('90-123456'))


# # Question 13- Write a Python program to remove leading zeros from an IP address

# In[32]:


import re


# In[36]:


ip_address = '145.04.089.07'
string = re.sub('\.[0]*','.', ip_address)


# In[37]:


print(string)


# # Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.

# In[ ]:





# In[ ]:





# # Write a Python program to search some literals strings in a string. Go to the editor
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
# 

# In[38]:


import re


# In[39]:


pattern = ['fox', 'dog', 'horse']
text= 'The quick brown fox jumps over the lazy dog.'


# In[48]:


for pattern in pattern:
    print('Searching for "%s" in "%s"' % (pattern, text),)
    if re.search(pattern, text):
        print('matched')
    else:
        print('not unmatched')


# # Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
# 

# In[49]:


import re


# In[50]:


pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match= re.search(pattern, text)
tr= match.start()
pr= match.end()


# In[51]:


print('Found "%s" in "%s" from %d to %d' % (match.re.pattern, match.string, tr, pr))


# # Question 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.
# 

# In[52]:


import re


# In[53]:


text=  'Python exercises, PHP exercises, C# exercises'
Pattern= 'exercises'


# In[56]:


for match in re.findall(pattern, text):
    print('Found "%s" ' % match)


# In[ ]:





# # Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[57]:


import re


# In[58]:


txt = 'Apple prices, Banana prices, Guava prices'


# In[61]:


pattern = 'prices'
for i in re.finditer(pattern, txt):
    a= i.start()
    b= i.end()
    print('"%s" at %d:%d' % (txt[a:b], a, b))


# In[ ]:





# # Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[62]:


import re


# In[63]:


def convert_date_format(date):
    return re.sub(r'(\d{1,2})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
date = "2023-07-15"


# In[64]:


print("original date in YYYY-MM-DD Format: ", date)
print("new date in DD-MM-YYYY Format: ", convert_date_format(date))


# # Question 20- Write a Python program to find all words starting with 'a' or 'e' in a given string.

# In[65]:


import re


# In[66]:


text = "the punishment assigned to a defendant found guilty by a court, or fixed by law for a particular offence"


# In[67]:


list = re.findall("[ae]\w+", text)
print(list)


# # the punishment assigned to a defendant found guilty by a court, or fixed by law for a particular offence.

# In[68]:


import re


# In[69]:


text = "the punishment assigned to a defendant found guilty by a court, or fixed by law for a particular offence"


# In[73]:


for i in re.finditer("\d+", text):
    print(i.group(0))
    print("Index position:", i.start())


# In[ ]:





# # Question 22- Write a regular expression in python program to extract maximum numeric value from a string

# In[74]:


import re


# In[76]:


string = 'abc123xyz25lmnoq9820'


# In[77]:


number = re.findall('\d+', string)
number = map(int, number)
print("max_value:", max(number))


# 

# # Question 23- Write a Regex in Python to put spaces between words starting with capital letters

# In[78]:


import re


# In[79]:


def capital_letters(string):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", string)


# In[80]:


print(capital_letters("Making"))
print(capital_letters("Making All"))
print(capital_letters("Making All Beleive"))


# # Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[81]:


import re


# In[82]:


def pattern(string):
    code = '[A-Z]+[a-z]+$'
    if re.search(code, string):
        return "matched"
    else:
        return "unmatched"


# In[83]:


print(pattern('Abc'))
print(pattern('abc'))


# # Question 25- Write a Python program to remove duplicate words from Sentence using Regular Expression

# In[84]:


import re


# In[85]:


string_1 = "It is the best to be alone"


# In[86]:


regex = r'\b(\w+)(?:\w+\1\b)+'
y= re.sub(regex, r'\1', string_1)


# In[87]:


print(y)


# # Question 27-Write a python program using RegEx to extract the hashtags.
# Sample Text: text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# Output: ['#Doltiwal', '#xyzabc', '#Demonetization']
# 

# In[88]:


import re


# In[89]:


text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <U+00A0><U+00BD><U+00B1><U+0089> "acquired funds" No wo"""


# In[91]:


for x in re.findall(r'#(\w+)', text):
    print('#',x)


# # Question 30- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Output: Python:Exercises::PHP:exercises:
# 

# In[92]:


import re


# In[93]:


text = 'Apple prices, Banana prices'


# In[94]:


print(re.sub("[,.]", ":", text))


# In[ ]:




