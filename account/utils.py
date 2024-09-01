from django.core.mail import EmailMessage
import os

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['body'],
            from_email=os.environ.get("Email_FROM"),
            to=[data["to_email"]]
        )
        email.send()