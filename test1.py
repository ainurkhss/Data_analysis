import requests
from bs4 import BeautifulSoup

response = requests.get('https://wisdompetmed.com/',timeout=10000)

soup = BeautifulSoup(response.text)

print(soup.find('span', class_="phone").text)