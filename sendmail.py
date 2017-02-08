import smtplib
from_addr = 'inphoqusnow@gmail.com'
to_addr = 'david@someemail.com'
from_name = 'Krystan Hunter'
to_name  = 'Bob'
subject = 'Test Mail'
msg = ""
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""
message_to_send = message.format(from_name, from_addr, to_name,
 to_addr, subject, msg)
# Credentials (if needed)
username = 'itworked@gmail.com'
password = 'bootlegdesigner'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 