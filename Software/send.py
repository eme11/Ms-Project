import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from picamera import PiCamera
from time import sleep

COMMASPACE = ', '

def main():
    # Recording video to send
    
    camera = PiCamera()

    camera.start_preview()
    camera.start_recording('/home/pi/video.h264')
    sleep(10)
    camera.stop_recording()
    camera.stop_preview()
    
    sender = 'raspberrypi.camera.project@gmail.com'
    gmail_password = 'PassWord12'
    recipients = ['emese.mathe.07@gmail.com']
    
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Motion detected'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # List of attachments
    attachments = ['/home/pi/video.h264']

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    main()
