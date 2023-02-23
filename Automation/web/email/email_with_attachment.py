import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

# Email server parameters
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
FROM_ADDRESS = 'your_email@gmail.com'
PASSWORD = ''

# Login to email server
server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
server.ehlo()
server.starttls()
server.login(FROM_ADDRESS, PASSWORD)

# Message parameters
TO_ADDRESS = 'target_email@...'
SUBJECT = 'Subject'
CONTENT = """
Content
"""

# Create email message
msg = MIMEMultipart()
msg['From'] = FROM_ADDRESS
msg['To'] = TO_ADDRESS
msg['Subject'] = SUBJECT
body = MIMEText(CONTENT, 'html')
msg.attach(body)

# Attach file to email
FILE_PATH = r"path"
FILE_NAME = 'file.txt'
attachment = open(FILE_PATH, 'rb')
att = MIMEBase('application', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)
att.add_header('Content-Disposition', f'attachment; filename="{FILE_NAME}"')
msg.attach(att)

# Send email
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print("Email sent!")
