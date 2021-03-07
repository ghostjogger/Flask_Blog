import smtplib
from twilio.rest import Client
import os

TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.environ.get('TWILIO_VIRTUAL_NUMBER')
TWILIO_VERIFIED_NUMBER = os.environ.get('TWILIO_VERIFIED_NUMBER')
MAIL_PROVIDER_SMTP_ADDRESS = os.environ.get('MAIL_PROVIDER_SMTP_ADDRESS')
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_email(self, name, email, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="ghostjogger@gmail.com",
                    msg=f"Subject:New Message from Stephen's Blog contact form\n\nFrom: {name}"
                        f"\nEmail address: {email} \n\nMessage: {message}".encode('utf-8')
                )