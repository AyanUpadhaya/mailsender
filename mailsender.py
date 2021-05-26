import smtplib,ssl

#smtp server address
smtp_server="smtp.gmail.com"
port=587 #for starttls

sender_email="ayanU881@gmail.com"
password="ayanU2005"
reciver_email="ayanupadhaya2010@gmail.com"
message=input("Enter your message:")
#create a secure ssl context

context=ssl.create_default_context()

#try to login to server and send mail

try:
	server=smtplib.SMTP(smtp_server,port)
	server.ehlo()#can be commited
	server.starttls(context=context)#secure the connection
	server.ehlo()
	server.login(sender_email,password)
	server.sendmail(sender_email,reciver_email,message)
except Exception as e:
	print(e)

finally:
	server.quit()
	print('Success')
