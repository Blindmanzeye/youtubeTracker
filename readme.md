This is a chrome web extention + flask server that will track in seconds how long you spend on either youtube/watch or youtube/shorts links in seconds and a script to send emails on mondays.

**DEPENDANCIES**
python (I used python 3.11)
flask (pip install flask)
flask_cors (pip install flask_cors)
timeTracker (pip install timeTracker)



notes for replication

in /webExtention/manifest, change the host permissions from localhost to whatever ip your server is running on
in /webExtention/script.js, change the fetch link from localhost to whatever ip your server is running at and change the track.json part to whatever your server is set to handle

in /sendMail.py:
- change myEmail to your email address
- change password to whatever authentication your email register provides
- gmailServer to the link that your email register uses for automatic emails //This script was repurposed from an older script where I only had gmail automation in mind
- gmailPort to whatever port your email register uses for automatic emails
- sendMail to contain email address(es) you want to send the email to

notes for /timeDisplay.py
- Since I originally planned for the server to be hosted on a linux machine, I designed the script in such a way that I can have it scheduled to run every day using cron. If you want to use this, either use cron
another scheduler or edit the script such that it can run in the background and execute in a timely fashion

notes for /timeTracker.py
- if you want to change the json file name, you will have to edit the filename in your directory, in the loadJson() and writeToJson() function declarations, @app.route() decorator, the CORS thing, and the script.js file
- I currently have the the duration reassignment under a try except block that catches all exceptions and only displays a log that something went wrong but doesnt spit an error code. This was mainly done for the purposes of testing and you may feel free
to modify the except block
- feel free to change the server port just make sure you also change it in your script.js file
