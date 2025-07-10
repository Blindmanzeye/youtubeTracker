import smtplib
from time import strftime, gmtime
from timeTracker import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail():
    myEmail = "example@gmail.com"
    myPassword = "some mail app code"

    gmailServer = "smtp.gmail.com"
    gmailPort = 587

    my_server = smtplib.SMTP(gmailServer, gmailPort)
    my_server.ehlo()
    my_server.starttls()

    my_server.login(myEmail, myPassword)
    textContent = f"""
    Hello. This is an Automated Emailing Service.
    This message is sent from a python script
    This message will be sent weekly writing to you the time he spent on youtube. 

    Please note that just because Rafsun is on youtube does not mean he is just watching. This is also time spent with youtube open while doing other things,
    watching, or learning by using youtube as a source for tutorials, math, and other things to learn.

    The time spent on youtube This Week is: {loadJson()["duration"]} Seconds
    or in hh:mm:ss:
    {strftime("%H:%M:%S", gmtime(loadJson()["duration"]))}
    """

    sendMail = ["mailRecipiants@mail.com"]
    message = MIMEMultipart()
    message["From"] = myEmail
    message["To"] = sendMail
    message["Subject"] = "Automated Youtube Tracking Time"

    message.attach(MIMEText(textContent, "plain"))


    my_server.sendmail(from_addr= myEmail, to_addrs=sendMail, msg=message.as_string())

    my_server.quit()