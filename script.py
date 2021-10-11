import smtplib


def send(FROM, TO, SUBJECT, TEXT, USERNAME, PASSWORD):
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (
        FROM, ", ".join(TO), SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROM, TO, message)
    server.quit()


def begin():
    uname = input("Please enter your username: ")
    pwd = input("Please Enter your account password: ")
    FROM = input("Please Enter the From data: ")
    to = input("Please Enter to whom I need to send the mail: ")
    sub = input("Please Enter the Email Subject: ")
    text = input("Please Enter the Message Body: ")
    send(FROM, to, sub, text, uname, pwd)


# Example
# send("FROM Text", receiver@gmail.com, "Subject", "blah blah", "username", "password")

if __name__ == "__main__":
    begin()
