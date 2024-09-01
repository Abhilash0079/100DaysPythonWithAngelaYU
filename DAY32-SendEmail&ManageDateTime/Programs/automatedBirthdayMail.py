import datetime as dt
import pandas
import random
import smtplib


MY_EMAIL = "abhilashkumar213@gmail.com"
MY_PASSWORD = "oswd xlcs fxlp dlvu"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY32-SendEmail&ManageDateTime/Resources/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY32-SendEmail&ManageDateTime/Resources/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{content}"
        )
