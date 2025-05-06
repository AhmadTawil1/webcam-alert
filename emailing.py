import imghdr
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials from environment variables
PASSWORD = os.getenv('EMAIL_PASSWORD')
SENDER = os.getenv('EMAIL_SENDER')
RECEIVER = os.getenv('EMAIL_RECEIVER')

def send_email(image_path):
    # Check if credentials are configured
    if not all([PASSWORD, SENDER, RECEIVER]):
        print("Error: Email credentials not configured. Please set up your .env file.")
        return

    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image",
                                 subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

