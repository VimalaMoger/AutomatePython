import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn))
conn.ehlo()
conn.starttls()  #send encrypted password
conn.login('mvt7@gmail.com','iu78')
conn.sendmail('mvt7@gmail.com', 'abc@gmail.com', 'subject: hi from pycharm')
conn.quit()