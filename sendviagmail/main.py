#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sending mail via gmail.
main function
"""

import smtplib
import email.mime.text



# -----------------------------------------------------------------------------
def create_message(from_addr, to_addr, subject, body):
	"""
	create mail message
	"""

	msg = email.mime.text.MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = to_addr

	return msg



# -----------------------------------------------------------------------------
def send_via_gmail(from_addr, to_addr, password, msg):
	"""
	send via gmail
	"""

	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(from_addr, password)
	s.sendmail(from_addr, [to_addr], msg.as_string())
	s.close()

	return



# -----------------------------------------------------------------------------
def main():
	"""
	main function
	"""

	from_addr = "from@test.com"
	password = "password"
	to_addr = "to@test.com"
	title = "title"
	body = "body"

	msg = create_message(from_addr, to_addr, title, body)

	send_via_gmail(from_addr, to_addr, password, msg)

	return 0
