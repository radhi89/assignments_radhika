
import re 
  
# Make a regular expression 
# for validating an Email 
regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email =input("Enter a mail id: ")


def Check(email):
	if(re.search(regex,email)):  
		print("Valid Email")  
          
	else:  
		print("Invalid Email")  

Check(email)