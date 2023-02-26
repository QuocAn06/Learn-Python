import smtplib
import datetime as dt
import random as rd

DOMAIN_SMTP = "smtp.gmail.com"
DOMAIN_PORT = 587
MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE____"
PARTNER_EMAIL = "___PARTNER_EMAIL_HERE____"
EMAIL_SUBJECT = "Monday Motivation"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("./data/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = rd.choice(all_quotes)

    print(quote)
    with smtplib.SMTP(DOMAIN_SMTP, DOMAIN_PORT) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=PARTNER_EMAIL,
            msg=f"Subject:{EMAIL_SUBJECT}\n\n{quote}"
        )












# import smtplib
# import datetime as dt
#
# # # ------------------- CONSTANTS -------------------
# # DOMAIN_SMTP = "smtp.gmail.com"
# # DOMAIN_PORT = 587
# #
# # MY_EMAIL = "sorry8699@gmail.com"
# # MY_PASSWORD = "zuuxlcqvdwtnvrtx"
# # PARTNER_EMAIL = "lenguyenquocan116@gmail.com"
# #
# #
# # # ---------------- CONNECT EMAIL DOMAIN ----------------
# # with smtplib.SMTP(EMAIL_SMTP, port=EMAIL_PORT) as connection:
# #     connection.starttls()
# #     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
# #     connection.sendmail(
# #         from_addr=MY_EMAIL,
# #         to_addrs=PARTNER_EMAIL,
# #         msg="Subject:Hello\n\nThis is the body of my email."
# #     )
#
# now = dt.datetime.now()
# day = now.day
# year = now.year
#
# date_of_birth = dt.datetime(year=1997, month=6, day=11)
#
# print(date_of_birth)
