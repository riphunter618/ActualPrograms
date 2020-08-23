import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = 'dumbass.idiot69@gmail.com'
    msg['from'] = user
    password = 'jrhxzexrtgbzuyss'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    # server.sendmail(user, '9849591665@tmomail.net', msg)
    server.quit()


email_alert('Hello', 'Hello world', '+919959380581@airtelap.in')
