import smtplib
from twilio.rest import Client

TWILIO_SID = "AC6b424e68dcb2a4407b3e7f3b5d9e9dc1"
TWILIO_AUTH_TOKEN = "1760502578329d3f400dec60dbdd0433"
TWILIO_VIRTUAL_NUMBER = "+12525125598"
TWILIO_VERIFIED_NUMBER = "+447595182215"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "ocktosh1968@gmail.com"
MY_PASSWORD = "19meikle78"

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