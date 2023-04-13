import smtplib
import os
from email.message import EmailMessage

@app.route('/send-email', methods=['POST'])
def send_email():
    # Get the form data submitted by the user
    name = request.form['name']
    email = request.form['email']
    phone = request.form['number']
    message = request.form['message']

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
    
if __name__ == '__main__':
    app.run(debug=True)
