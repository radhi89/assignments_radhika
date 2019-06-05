#Fetch image url, country name from the URL http://example.webscraping.com/ using beautifulsoup
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://example.webscraping.com/')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img')
country_name = bs.find_all('td')

names = [name.get_text() for name in country_name]	
image_url = [image['src'].split() for image in images]
list_image = dict(zip(names,image_url))

print("{country_name : image url } = ",list_image)