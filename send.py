import sys
import requests
from datetime import datetime

from formatting import format_msg
from send_mail import send_mail


def send(name=None,website=None,to_mail=None,verbose=False):
    assert to_mail != None

    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name,website,to_mail)

    #send message
    try:
        send_mail(text=msg,to_emails=[to_mail],html=None)
        sent = True
    except:
        sent = False

    return sent



if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    response = send(name, to_mail=email, verbose=True)
    print(response)
