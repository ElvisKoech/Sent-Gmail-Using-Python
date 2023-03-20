from email.message import EmailMessage
from email.mime.application import MIMEApplication
from os.path import basename
from app2 import password
import smtplib
import ssl

email_sender = "Johndoe@gmail.com"
email_password = password
email_receiver = "test@gmail.com"
subject = "Junior Software Developer Resume"
body = """
Please find attached a revised resume. If you have any problems, don't hesitate to reach out.


Yours Truly.
"""

# Create the email message
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Set the content type to multipart/mixed
em.set_content("", subtype='mixed')

# Add the PDF attachment
with open("Junior Software Developer-Resume.pdf", "rb") as f:
    attachment = MIMEApplication(f.read(), _subtype="pdf")
    attachment.add_header("Content-Disposition", "attachment", filename=basename("Junior Software Developer-Resume.pdf"))
    em.add_attachment(attachment)

# Connect to the SMTP server
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
