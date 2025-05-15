# # send_email.py
# import smtplib
# import sys
# from email.message import EmailMessage

# recipient = sys.argv[1]
# filename = sys.argv[2]

# with open(filename, 'r') as f:
#     body = f.read()

# msg = EmailMessage()
# msg.set_content(body)
# msg['Subject'] = "System Doctor - Report"
# msg['From'] = 'garggourav012@gmail.com'   # your sender email
# msg['To'] = recipient

# # Gmail SMTP server example
# with smtplib.SMTP('smtp.gmail.com', 587, timeout=10) as smtp:
#     smtp.starttls()
#     smtp.login('garggourav012@gmail.com', 'zlox ajyq llie iqvf')
#     smtp.send_message(msg)

# send_email.py
import smtplib
import sys
from email.message import EmailMessage
import ssl

recipient = sys.argv[1]
filename = sys.argv[2]
# recipient = "garggourav012@gmail.com"
# filename = "system_monitor.log"

# Read the body from file
with open(filename, 'r') as f:
    body = f.read()

# Compose message
msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = "System Doctor - Report"
msg['From'] = 'garggourav012@gmail.com'
msg['To'] = recipient

# Create secure SSL context
context = ssl.create_default_context()

# Use SSL (port 465) instead of starttls (port 587)
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login('garggourav012@gmail.com', 'zlox ajyq llie iqvf')  # use app password
    smtp.send_message(msg)

print("✅ Email sent successfully.")
