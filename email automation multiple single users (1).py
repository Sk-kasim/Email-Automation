import smtplib
print(smtplib.__file__)
from email.mime.text import MIMEText

From="srijasanku@gmail.com"
password="oarn mxpb duev jxcl"

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(From,password)

to=["kasimsk4351@gmail.com","sankuvishnu12@gmail.com"]
subject="Mail from Srija"
message=f" Hii everyone you all are selected to codegnan IT solutions"

#MIMEText:
for email in to:
    msg=MIMEText(message)
    msg["subject"]=subject
    msg["from"]=From
    msg["to"]=email
    
    server.sendmail(From,email,msg.as_string())
    
    print(f"mail sent suceesfully to {email}")
    
server.quit()
