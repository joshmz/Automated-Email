import smtplib
def send_mail(Subject,Message):
    #INITIALISE EMAIL SERVER
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #DICTATE WHICH EMAIL TO USE
    server.login('','')# 1. FROM EMAIL 2. PASSWORD

    #MESSAGE FORMAT
    msg = (f"Subject: {Subject}\n\n{Message}")

    #DICTATE FROM AND TO EMAIL
    server.sendmail('','',msg)# 1.FROM EMAIL 2. TO EMAIL

    server.quit()
