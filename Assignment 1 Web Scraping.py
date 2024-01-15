#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
url = "https://www.dineout.co.in"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements containing the details you want to scrape
restaurant_names = soup.find_all('h2', class_='restnt-name ellipsis')
cuisines = soup.find_all('span', class_='double-line-ellipsis')
locations = soup.find_all('span', class_='double-line-ellipsis')
ratings = soup.find_all('span', class_='rating-value')
image_urls = soup.find_all('img', class_='img-responsive')

# Create empty lists to store the scraped data
restaurant_list = []
cuisine_list = []
location_list = []
rating_list = []
image_url_list = []

# Extract the data from the elements and append them to the respective lists
for name in restaurant_names:
  restaurant_list.append(name.text.strip())

for cuisine in cuisines:
  cuisine_list.append(cuisine.text.strip())

for location in locations:
  location_list.append(location.text.strip())

for rating in ratings:
  rating_list.append(rating.text.strip())

for image in image_urls:
  image_url_list.append(image['src'])

# Create a dictionary from the lists
data = {
  'Restaurant Name': restaurant_list,
  'Cuisine': cuisine_list,
  'Location': location_list,
  'Ratings': rating_list,
  'Image URL': image_url_list
}

# Create a dataframe from the dictionary
df = pd.DataFrame(data)

# Print the dataframe
print(df)


# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the Wikipedia page
url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the header tags (h1 to h6) using the find_all method
header_tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

# Extract the text from the header tags and store them in a list
header_texts = [tag.get_text() for tag in header_tags]

# Create a data frame using pandas
df = pd.DataFrame(header_texts, columns=["Header"])

# Display the data frame
print(df)


# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.cnbc.com/world/?region=world"
response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all("div", class_="Card-titleContainer")


headlines = []
times = []
links = []


for article in articles:
  headline = article.find("a").text.strip()
  headlines.append(headline)
  
  time = article.find("a").text.strip()
  times.append(time)

  link = article.find("a")["href"]
  links.append(link)


data = {
  "Headline": headlines,
  "Time": times,
  "News Link": links
}
df = pd.DataFrame(data)

print(df)


# #### 

# In[5]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
url = "https://presidentofindia.nic.in/former-presidents.htm"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the information
table = soup.find("table")

# Create empty lists to store the data
names = []
terms = []

# Iterate over each row in the table
for row in table.find_all("tr")
  # Extract the name and term of office from the columns
  columns = row.find_all("tr")
  name = columns[0].text.strip()
  term = columns[1].text.strip()
  
  # Append the data to the respective lists
  names.append(name)
  terms.append(term)

# Create a data frame using the lists
data = {"Name": names, "Term of Office": terms}
df = pd.DataFrame(data)

# Display the data frame
print(df)


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

team_data = []
table = soup.find("table", class_="table")
rows = table.find_all("tr")

for row in rows[1:11]:
  cells = row.find_all("td")
  team = cells[1].text.strip()
  matches = cells[2].text.strip()
  points = cells[3].text.strip()
  rating = cells[4].text.strip()
  team_data.append([team, matches, points, rating])

df = pd.DataFrame(team_data, columns=["Team", "Matches", "Points", "Rating"])
print(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




