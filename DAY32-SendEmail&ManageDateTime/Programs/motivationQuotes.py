import smtplib
import datetime as dt
import random

MY_EMAIL = "singh.aman130791@gmail.com"
MY_PASSWORD = "vpqf fumo onac rkrz"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY32-SendEmail&ManageDateTime/Resources/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )

