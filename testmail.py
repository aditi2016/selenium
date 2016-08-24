import smtplib
from smtplib import SMTPException

sender = 'aditilahoria@gmail.com'
receivers = ['aditi@blueteam.in']

message = """From: From Person <den.callanan@gmail.com>
To: To Person <callanden@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    print("trying host and port...")

    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.login("aditilahoria@gmail.com", "killbill12345")

    print("sending mail...")

    smtpObj.sendmail(sender, receivers, message)

    print("Succesfully sent email")

except smtplib.SMTPException:
    print("Error: unable to send email")
    import traceback
    traceback.print_exc()