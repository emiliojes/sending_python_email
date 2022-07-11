import os
from email.message import EmailMessage
import ssl
import smtplib

email_from = 'emiliojes@gmail.com'
email_password = 'fzpfwdlmkcoizmgs'
email_to = 'emiliojes@oxford.edu.pa'

subject = 'Check my video on Youtube'

message = """ I just upload a video on Youtube"""

em = EmailMessage()
em['From'] = email_from
em['To'] = email_to
em['Subject'] = subject
em.set_content(message)

contexts = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexts) as smtp:
    smtp.login(email_from, email_password)
    smtp.sendmail(email_from, email_to, em.as_string())