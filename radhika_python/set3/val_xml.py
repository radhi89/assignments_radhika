#Fetch data from the URL https://www.w3schools.com/xml/simple.xml and print name, price of each item.

from BeautifulSoup import BeautifulSoup as BS
import urllib

response = urllib.urlopen('https://www.w3schools.com/xml/simple.xml')

# do something
soup = BS(response)
elem = soup.findAll('food')
print(elem)

response.close()