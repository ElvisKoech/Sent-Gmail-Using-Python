# Sent-Gmail-Using-Python

This code is a Python program that sends an email with an attached PDF file using the Simple Mail Transfer Protocol (SMTP) and the email library. The code first sets up the email sender's email address and password, the recipient's email address, the email subject, and the email message body.

The email message object is then created using the EmailMessage() function, and the email sender, receiver, subject, and body are set using the appropriate methods of the EmailMessage object.

The email message's content type is then set to multipart/mixed, indicating that it contains both plain text and attachments.

The PDF file is attached to the email message using the MIMEApplication() function to create a MIME object representing the attachment. The attachment object is then added to the email message using the add_attachment() method.

Finally, the email is sent using the SMTP server smtp.gmail.com with port 465 and SSL encryption. The program logs in to the email account using the sender's email address and password and sends the email message using the send_message() method of the SMTP object.