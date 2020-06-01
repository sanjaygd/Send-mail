import os
import smtplib

EMAIL_ADDRESS = os.environ.get("USER_MAIL_ID")
EMAIL_PASSWORD = os.environ.get("USER_PASSWORD")

# with smtplib.SMTP('smtp.gmail.com',587) as smtp: # line 7,9,10,11 should be there if we don't use line 8
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    subject = 'Summer vacation'
    body = "How is everything going on in this summer..."

    msg = f'Subject : {subject}\n\n {body}'

    smtp.sendmail(EMAIL_ADDRESS, 'Dev py <sanjaygd35@gmail.com>',msg)

    print('Message Sent...!')

