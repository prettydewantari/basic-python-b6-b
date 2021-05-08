import smtplib

sender_email = "prettydewantari9@gmail.com"
rec_email = "prettydewantari9@gmail.com"
password = "PTD271000"
message = "this is sent from python"

with smtplib.SMTP('smtp.gamil.com', 587) as smtp
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_email, password)

    smtp.sendemail(sender_email, rec_email, message)