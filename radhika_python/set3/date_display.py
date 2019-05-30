#Write a Python program to print yesterday, today, tomorrow.

import datetime
from datetime import timedelta


today = datetime.datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("yesterday : ",yesterday.strftime("%A, %d. %B %Y"))
print("Today : ",today.strftime("%A, %d. %B %Y"))
print("Tomorrow: ",tomorrow.strftime("%A, %d. %B %Y"))
