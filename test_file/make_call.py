import pandas as pd
from datetime import datetime
import smtplib
from email.message import EmailMessage


print('importfile', __name__)        
def send_email():
   GMAIL_ID = 'prabakarann.2702@gmail.com'
   GMAIL_PWD = 'Praba@27'

   email = EmailMessage()
   email['Subject'] = 'TRYING'
   email['From'] = GMAIL_ID
   email['To'] = 'prabakaran.g@kgisl.com'
   email.set_content('WISH YOU HAPPY BIRTHDAY')

   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_obj:
       gmail_obj.ehlo()
       gmail_obj.login(GMAIL_ID, GMAIL_PWD)
       gmail_obj.send_message(email)
   print('Email sent to ' + str('recipient') + ' with Subject: \''
         + str('subject') + '\' and Message: \'' + str('msg') + '\'')




if __name__ == '__main__':      
   print('tesing')
   
   send_email()