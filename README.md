# Internship Application Sender

A simple script that sends your internship application to a list of companies.

## Description

If you want to send your internship application to lots of companies and you are too lazy this script is for you. The script uses "Simple Mail Transfer Protocol" (SMTP for short) to send emails.

## Getting Started

### What do you need

* First you'll need an email account to send the emails from.
* Then you'll need an introduction text where you give brief info about yourself named "introduction.txt".
* Next you'll need your CV as a pdf file named "cv.pdf".
* And lastly you'll need a list of emails to send your application to.

### Configuring the script

* You don't need to touch the script file itself if you're using Gmail as your email service. If not than you'll need to change your email service in the script file.
* Put your introduction text to the "introduction.txt" file.
* Put your cv to the script folder and name it "cv.pdf".
* Put each email adress you want to send your application to on a seperate line in "mails.txt"
* Put your name, email and email password to "credentials.py" file.
* Congratulations, you're good to go!

### Executing the script

* To run the program simply type ```python main.py``` on the command line.
* Then the program will start sending your internship application (your introduction text and CV) to each email in the "mails.txt".
* Mails that are succesfully sent will be logged to "sent.txt" and mails that are failed to send will be logged to "failed.txt".