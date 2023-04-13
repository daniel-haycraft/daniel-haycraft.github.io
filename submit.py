import smtplib
import os
from email.message import EmailMessage
from flask import Flask, request, render_template

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587
app = Flask(__name__)

# Set up the email message
sender_email = "dhcopy1@gmail.com"
recipient_email = "dhcopy1@gmail.com"
message_subject = "contact"


@app.route('/send-email', methods=['GET','POST'])
def send_email():
    if request.method =='POST':
            
        name = request.form['name']
        email = request.form['email']
        phone = request.form['number']
        message = request.form['message']

        msg = EmailMessage()
        msg.set_content(message)
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = message_subject
        msg.add_alternative(f"<p>Name: {name}</p><p>Email: {email}</p><p>Phone Number: {phone}</p><p>Message: {message}</p>", subtype='html')

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login("dhcopy1@gmail.com", os.environ['SMTP_PASSWORD'])
            server.send_message(msg)
    
    return 'success!'
    
if __name__ == '__main__':
    app.run(debug=True)


