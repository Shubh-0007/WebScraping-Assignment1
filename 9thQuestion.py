#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


url = 'https://www.dineout.co.in/delhi-restaurants/buffet-special'

page = requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")

soup = BeautifulSoup(page.content, 'html.parser')

restaurant_name = soup.find_all('a', class_='restnt-name ellipsis')
cuisine = soup.find_all ('li', class_='restaurants in North Indian, restaurants in Chines')
location = soup.find_all ('div', class_='res-info-location clearfix')
ratings = soup.find_all ('div', class_='res-info-detail')
image_url = soup.find_all ('div', class_='rest-img')

for i in range(len(restaurant_name)):
    print("Restaurant Name:", restaurant_name[i].h3.text)
    print("Cuisine:", cuisine[i].text.strip())
    print("Location:", location[i].text.strip())
    print("Ratings:", ratings[i].text.strip())
    print("Image URL:", image_url[i].img['src'])
    print("\n")


# In[ ]:




