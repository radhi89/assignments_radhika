import urllib.request

response = urllib.request.urlopen('https://www.pythonforbeginners.com/')
print(response.info())
html = response.read()
# do something
print(html)
response.close()  # best practice to close the file
