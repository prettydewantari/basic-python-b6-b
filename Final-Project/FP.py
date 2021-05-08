import smtplib
import imghdr
import my_file
from email.message import EmailMessage

urlfile = open ("contacts.txt", "r+")
mailList = [i.strip() for i in urlfile.readlines()]

msg = EmailMessage()
msg['Subject'] = 'Python!'
msg['From'] = my_file.EMAIL_ADDRESS
msg['To'] = mailList

msg.set_content('This is email from python')
with open('hello.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(my_file.EMAIL_ADDRESS, my_file.EMAIL_PASSWORD)
    smtp.send_message(msg)