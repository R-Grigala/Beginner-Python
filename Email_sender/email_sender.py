from email.message import EmailMessage
from decouple import config, Csv
import ssl
import smtplib

email_sender = config('Gmail')
email_password = config('Gmail_password')

email_receiver = 'roma.grigalashvili@iliauni.edu.ge'

subject = "Dont forget to subscribe"
body = """ 
When you watch a video, please hit subscribe
"""
email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())