import smtplib

EMAIL_SMTP = "smtp.gmail.com"
EMAIL_PORT = 587

my_email = "sorry8699@gmail.com"
my_password = "zuuxlcqvdwtnvrtx"
partner_email = "lenguyenquocan116@gmail.com"


with smtplib.SMTP(EMAIL_SMTP, port=EMAIL_PORT) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=partner_email,
        msg="Subject:Hello\n\nThis is the body of my email."
    )

