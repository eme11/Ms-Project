#it is used for email sending and creatings
import os
import sys
import optparse
import smtplib
import time
import datetime
import email

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import Encoders

def create_message(user, recipients, subject, body):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body))
    return msg

#using this function we can attach a file to the email
def send_mail_attachment(user, password, recipients, subject, body, files):
    msg = create_message(user, recipients, subject, body)
    
    part = MIMEBase('application', "octet-stream")
    fo=open(files,"rb")
    part.set_payload(fo.read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(files))
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, recipients, msg.as_string())
    server.close()
    print('Sent email to %s' % (', '.join(recipients)))

#we can inly send text using this function
def send_mail_simple(user, password, recipients, subject, body):
    msg = create_message(user, recipients, subject, body)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, recipients, msg.as_string())
    server.close()
    print('Sent email to %s' % (', '.join(recipients)))
