#Write a program to find all mobile number inside a string.
import re

string = input("Enter the string: ")
mobile_no = re.findall(r"[0-9]{10}",string)
print("Mobile number inside string is : ",mobile_no)