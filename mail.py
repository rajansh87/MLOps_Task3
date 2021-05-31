import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("xyz@gmail.com", "*********")


    # message
message = "Your accuracy is less than 90% .Try again"


    # sending the mail
s.sendmail("xyz@gmail.com", "abc@gmail.com", message)


    # terminating the session
s.quit()
