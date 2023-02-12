from datetime import datetime
import pandas

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("./data/birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}

