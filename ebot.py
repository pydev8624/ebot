import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ekey import *

# Your credentials
gmail_user = gmail
gmail_password = ekey  # NOT your Gmail password

# Email details
to_email = email
subject = 'e-bot'
body = 'first enable two vertification on your gmail security then visit https://myaccount.google.com/apppasswords take pass generated then git me'

# Create the message
message = MIMEMultipart()
message['From'] = gmail_user
message['To'] = to_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    # Connect to Gmail SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(gmail_user, gmail_password)
        server.send_message(message)
        print('Email sent successfully!')

except Exception as e:
    print(f'Error: {e}')
