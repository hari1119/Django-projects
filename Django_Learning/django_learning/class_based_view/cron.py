import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django_learning.settings import *

def my_task():
    # create SMTP object
    smtp_obj = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)

    # initiate SMTP conversation
    smtp_obj.ehlo()

    # start TLS encryption
    smtp_obj.starttls()

    # login to SMTP server
    smtp_obj.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

    # create message object
    msg = MIMEMultipart()

    # set message body
    body = "Hello, this is a test message!"
    msg.attach(MIMEText(body, 'plain'))

    # set message headers
    msg['From'] = "prabakarann.2702@gmail.com"
    msg['To'] = "prabakarann.2702@gmail.com"
    msg['Subject'] = "Test message from Sendinblue SMTP"

    # send the message
    smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())

    # close the SMTP connection
    smtp_obj.quit()

