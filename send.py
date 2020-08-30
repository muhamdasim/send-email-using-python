import pandas as pd
import smtplib
import ssl


#read a text file having recipient email's
def readRecipientEmails():
    df=pd.read_csv('recipient.csv')
    emails=df['Email'].values.tolist()

    return emails



def smtServer():
    smtp_server='smtp.gmail.com'
    port=465
    sender_email = "i180508@nu.edu.pk"  # Enter your address
    receiver_email = "asimgujjarpk@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = """\
    Subject: 

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

recipientEmails=readRecipientEmails()


smtServer()