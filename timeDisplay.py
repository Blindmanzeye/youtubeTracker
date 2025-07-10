from datetime import datetime
from sendMail import *


# On your linux machine, use cron to schedule this script

def fileData():
    with open("weekDone.txt", "r") as f:
        return bool(f.read())


def writeToFile(data):
    with open("weekDone.txt", "w") as f:
        f.write(data)


if not fileData() and datetime.now().weekday() == 0 and datetime.now().hour == 0:
    # Do stuff
    sendMail()
    print("Ran Email Sent")
    writeToFile("True")
    pass

if fileData() and datetime.now().weekday() == 1:
    print("Ran File Flip")
    writeToFile("")
    pass
