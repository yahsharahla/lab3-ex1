import smtplib

#message information
fromaddr = 'artnellebanks@gmail.com'
toaddrs = 'artnellebanks@gmail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
fromname = 'artnellebanks@gmail.com'
toname = 'artnellebanks@gmail.com'
subject = 'wicked'
msg = """young general what a gwaan"""
messagetosend = message.format(fromname,fromaddr,toname,toaddrs,subject,msg)
# Credentials (if needed)
username = 'artnellebanks@gmail.com'
password = 'syjtcihrewdmjrxt'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, messagetosend)
server.quit()