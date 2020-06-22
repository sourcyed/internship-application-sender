import requests
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from credentials import my_name, my_mail, my_password

def login():
    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s.ehlo()
    s.login(my_mail, my_password)
    return s

def message(mail, content, pdf_path):
    msg = MIMEMultipart()
    msg["From"] = my_name
    msg["To"] = mail
    msg["Subject"] = "Internship Application"
    text = MIMEText(content)
    msg.attach(text)
    with open(pdf_path, "rb") as f:
        attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename=str(pdf_path))
    msg.attach(attach)
    return msg

def send_application(s, mail, msg):    
    s.sendmail(msg["From"], msg["To"], msg.as_string())

def send_mails(s):
    with open("sent.txt", 'w') as sent:
        with open("failed.txt", 'w') as failed:
            for mail in mails:
                if "@" in mail:
                    try:
                        msg = message(mail, introduction, cv_path)
                        send_application(s, mail, msg)
                        sent.write(mail + "\n")
                        print("Mail sent.")
                    except Exception as e:
                        failed.write(mail + "\n")
                        print("Mail couldn't sent.", e)

mails = open("mails.txt", 'r', encoding="utf-8").read().split("\n")
introduction = open("introduction.txt", 'r', encoding="utf-8").read()
cv_path = "cv.pdf"
print(mails)

try:
    s = login()
    print("Signed in.")
    send_mails(s)
except Exception as e:
    print("Couldn't sign in.", e)
    exit()