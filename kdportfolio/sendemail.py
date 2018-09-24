import sendgrid
import os
from sendgrid.helpers.mail import *
from keys import SENDGRID_API_KEY


def send_email(name, fromemail, content):
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    from_email = Email("message@kyledupont.io")
    to_email = Email("dupontke@gmail.com")
    subject = "New IO message from {}, {}".format(name, fromemail)
    content = Content("text/plain", content)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    send_email.code = response.status_code
    print(response.status_code)


#send_email("billy", "bily128282@gmail.com", "here is my message")

# print(response.body)
# print(response.headers)
