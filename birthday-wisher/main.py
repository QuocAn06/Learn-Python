from datetime import datetime
import pandas
import random

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("./data/birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}
if today_tuple in birthday_dict:
    file_path = f"./data/letter_templates/letter_{random.randint(1,3)}.txt"
    