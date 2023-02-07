from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'sihleduma0@gmail.com'
email_password = 'wanx oupq eilx hryl'

email_receiver = 'setasah682@keshitv.com'

subject = 'Internship acceptance'
body = """
We are pleased to let you know that you 
have been selected as a candidate for 
the Junior Python Developer position
"""

em = EmailMessage()
em['FROM'] = email_sender
em['TO'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

