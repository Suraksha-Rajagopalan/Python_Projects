import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = input('enter sender mail address:')  # Enter your address
receiver_email = input('enter receiver mail address:')  # Enter receiver address
password = input("Type your password and press enter: ")
message =input('enter myour message:')

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
