#!/usr/bin/env python
# coding: utf-8

# In[8]:


from urllib.request import urlopen


# In[9]:


from bs4 import BeautifulSoup


# In[10]:


html = urlopen('https://en.wikipedia.org/wiki/Main_Page')


# In[11]:


bs = BeautifulSoup(html, "html.parser")


# In[12]:


titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])


# In[13]:


print('List all the header tags :', *titles, sep='\n\n')


# In[ ]:




