import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("anshshriv22296@gmail.com", "**********")


    # message
message_success = "Achieved your desired accuracy without tweeking . Congrats "


    # sending the mail
s.sendmail("anshshriv22296@gmail.com", "rajansh87@gmail.com", message_success)


    # terminating the session
s.quit()
