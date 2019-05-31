#Fetch data from the URL https://www.w3schools.com/xml/simple.xml and print name, price of each item.

from lxml import html
import requests



page = requests.get('https://www.w3schools.com/xml/simple.xml')
tree = html.fromstring(page.content)

#This will create a list of food name
names = tree.xpath('//food/name/text()')
#This will create a list of prices
prices = tree.xpath('//food/price/text()')

food = dict(zip(names,prices))
print("Food items name and their prices : ",food)