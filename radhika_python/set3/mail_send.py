#function to send a mail
import smtplib 

def sendemail(sender,receiver,message):
	# creates SMTP session 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
  	# start TLS for security 
	s.starttls() 
  	# Authentication 
	s.login("*****", "*****") 
  	s.sendmail("radhika.sayone@gmail.com", "sradhi89@gmail.com", message) 
	# terminating the session 
	s.quit() 


sendemail("radhika.sayone@gmail.com", "sradhi89@gmail.com","hello how are you?")

