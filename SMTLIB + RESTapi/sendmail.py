#!/usr/bin/env python

import email
import smtplib
from cats import Catsfact


cote = Catsfact()

SMT_server = "smtp.gmail.com"
SM_port = 587
SMTP_username = "user@gmail.com"
SMTP_password = "user123"

sender = 'user@gmail.com'

receivers = ['user1@ukr.net', 'user2@gmail.com', 'user3@ukr.net']


message="""From: Moor moor Ko.
To:  For You
Subject: Facts about cats
"""
message += cote.TestGetCat()+ '''


With love
LCC: Lovers Club Cats
Have a nice day!
'''


server = smtplib.SMTP(SMT_server, SM_port)
server.starttls()
server.login(SMTP_username, SMTP_password)
server.sendmail(sender, receivers, message)
server.quit()
