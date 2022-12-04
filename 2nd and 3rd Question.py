#!/usr/bin/env python
# coding: utf-8

# In[21]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
 
 
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select('td.titleColumn')

ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]
 
 
 
 
list = []
 
for index in range(0, len(movies)):
     
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)

    data = {
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            
            }
    list.append(data)
 

for movie in list:
    print(movie['movie_title'],
          'Rating-'+
        movie['rating'], 'Year-' + movie['year'])
 
 
df = pd.DataFrame(list)
df.to_csv('imdb_top_250_movies.csv',index=False)


# In[2]:





# In[3]:





# In[ ]:




