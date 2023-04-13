import smtplib
import os
from email.message import EmailMessage

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587


# Set up the email message
sender_email = "dhcopy1@gmail.com"
recipient_email = "dhcopy1@gmail.com"
message_subject = "contact"
message_body = "This is a test email sent from Python."
msg = EmailMessage()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = message_subject
msg.set_content(message_body)


with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login("dhcopy1@gmail.com", os.environ['SMTP_PASSWORD'])
    server.send_message(msg)
    

