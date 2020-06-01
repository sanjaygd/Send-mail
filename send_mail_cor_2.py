import imghdr
import os
import smtplib
from email.message import EmailMessage



EMAIL_ADDRESS = os.environ.get("USER_MAIL_ID")
EMAIL_PASSWORD = os.environ.get("USER_PASSWORD")
contacts = ['sanjaygd35@gmail.com','sanjaygd96@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Sent it again'
msg['From'] = EMAIL_ADDRESS
msg['To']  = 'sanjaygd96@gmail.com'  # To send single user
# msg['To'] = ','.join(contacts)  #To send multiple user
msg.set_content("It's a new blog here looks so awsome...!")

msg.add_alternative("""\
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>This is testing mail to check html content</h2>
</body>
</html>

""", subtype='html')


# files = ['blog2.jpeg', 'blog3.jpg']

files = ['test.pdf']

for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    # msg.add_attachment(file_data, maintype='image',subtype=file_type,filename=file_name) #This is for sending images
    msg.add_attachment(file_data, maintype='application',subtype='octet-stream',filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)

print('Message Sent...!')

