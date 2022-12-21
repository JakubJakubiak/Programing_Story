# import requests
# from bs4 import BeautifulSoup

# URL = 'http://www.example.com'
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(id='results')


import requests
from bs4 import BeautifulSoup

URL = 'http://www.example.com'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.find_all(class_='item')

for item in items:
  print(item)
