import smtplib

#message information
fromaddr = ''
toaddrs = ''
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
fromname = ''
toname = ''
subject = ''
msg = """"""
messagetosend = message.format(fromname,fromaddr,toname,toaddrs,subject,msg)
# Credentials (if needed)
username = ''
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, messagetosend)
server.quit()