from datetime import datetime
import pandas
import random
import smtplib

DOMAIN_SMTP = "smtp.gmail.com"
DOMAIN_PORT = 587
MY_EMAIL = "sorry8699@gmail.com"
MY_PASSWORD = "zuuxlcqvdwtnvrtx"
EMAIL_SUBJECT = "Happy Birthday!!!"
THE_SIGNATURE = "An Le"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("./data/birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"./data/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        contents = contents.replace("[SIGNATURE]", THE_SIGNATURE)

    with smtplib.SMTP(DOMAIN_SMTP, DOMAIN_PORT) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:{EMAIL_SUBJECT}\n\n{contents}"
        )
