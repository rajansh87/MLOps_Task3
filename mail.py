import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("anshshriv22296@gmail.com", "*********")


    # message
message = "Your accuracy is less than 90% .Try again"


    # sending the mail
s.sendmail("anshshriv22296@gmail.com", "rajansh87@gmail.com", message)


    # terminating the session
s.quit()
