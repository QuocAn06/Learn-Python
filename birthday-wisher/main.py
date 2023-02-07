import smtplib

my_email = "sorry8699@gmail.com"
my_password = "zuuxlcqvdwtnvrtx"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="lenguyenquocan116@gmail.com", msg="Hello")
connection.close()
