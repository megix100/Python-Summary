#Don't name the file as e-mail.py. It is going to have an error
#https://www.youtube.com/watch?v=JRCJ6RtE3xU
#You have to turn on the option in the link below if it is gmail:
#https://myaccount.google.com/lesssecureapps?pli=1
#https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16137245#questions/9944584
import smtplib #An e-mail needs a server to receive and send it like the https in the web and smtplib here
import imghdr #It is needed to attach files in the e-mail
from email.message import EmailMessage #It is needed to send an e-mail

#Customizing your e-mail with automatic part
from string import Template
from pathlib import Path #similar to os module

#-------------------------------------------
contacts=["ciro_henrique14@hotmail.com", "cirohenrique14@hotmail.com"]
html=Template(Path("index.html").read_text())
#Path=Read the index.html file
#Template changes the variable #name in the index.html file
email= EmailMessage()
email['From']="Ciro Henrique Canha Teixeira"
email['To']=contacts
email['Subject ']="test python subject"
email.set_content(html.substitute({"name":"Tintin","age":"25"),"html")
#The variable name comes from the index.html, so we can personalize and change it depending of the person we are sending

#Adding image attachment to the e-mail
files=["charmander.jpg","pikachu.jpg"]
for file in files:
    with open (file,"rb") as f:
        file_data=f.read()
        file_type=imghdr.what(f.name) #Put the file in it
        file_name=f.name
    email.add_attachment(file_data, maintype="image",subtype=file_type,filename=file_name)
#-------------------------------

#Adding PDF attachment to the e-mail
files_pdf=["dummy.pdf"]
for file in files_pdf:
    with open (file,"rb") as f:
        file_data=f.read()
        # file_type=imghdr.what(f.name) #YOU DON'T NEED THIS LINE
        file_name=f.name
    email.add_attachment(file_data, maintype="application",subtype="octet-stream",filename=file_name)
#-------------------------------

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
    # This is the server where the e-mail is going to be sent from and the host is the person's e-mail you are sending it to
    # The port is going to be 587 or 465
    # smtp.ehlo()#Always this
    # smtp.starttls()#Encryption mechanism
    # smtp.ehlo()#Always this
    smtp.login("cirohenrique14@gmail.com","cirohen140595")
    #credentials for the e-mail
    smtp.send_message(email)
    print("all good")