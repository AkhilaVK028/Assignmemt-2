import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from schemas.models import Email

def send_email(body: str, email: Email):
    sender_email = "akhilavk028@gmail.com"
    sender_password = "bykqqbpbcqnnmvhf"
    receiver_email = email.rec_email

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email.subject


    # Add the body to the email
    message.attach(MIMEText(body, "plain"))

    try:
        # Create a secure connection to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(message)

        # Close the connection
        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"message": str(e)}

