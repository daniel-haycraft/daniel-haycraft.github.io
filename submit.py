import smtplib
import os
from email.message import EmailMessage
from flask import Flask, request, render_template

app = Flask(__name__)

app.secret_key = 'dev'

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587


# Set up the email message
sender_email = "dhcopy1@gmail.com"
recipient_email = "dhcopy1@gmail.com"
message_subject = "contact"
message_body = "This is email sent from Daniels Python."
msg = EmailMessage()


def contact():
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = message_subject
    name = request.form['name']
    email = request.form['email']
    phone = request.form['number']
    message = request.form['message']
    msg.set_content(name, email, phone, message, message_body)
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login("dhcopy1@gmail.com", os.environ['SMTP_PASSWORD'])
        server.send_message(msg)
    
    return 'success!'
    




