import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'devapp202026@gmail.com'
password = 'save1234'

def send_mail(text='Email body', subject='Hello World',from_email='Dev py <devapp202026@gmail.com>', to_emails=None, html = None):
    assert isinstance(to_emails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ','.join(to_emails)
    msg['Subject'] = subject
    print(subject, text)
    

    text_part = MIMEText(text, 'plain')
    msg.attach(text_part)
    if html != None:
        html_part = MIMEText("<h1> This done for testing purpose</h1>", 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()  

# with smtplib.SMTP() as server:
#     server.login()
#     pass