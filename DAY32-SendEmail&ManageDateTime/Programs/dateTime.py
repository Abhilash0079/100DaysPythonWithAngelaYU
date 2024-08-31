import datetime as dt

# Current date and time
now = dt.datetime.now()
year = now.year
print(now.month)
print(now.day)
print(now.weekday())
print(now)
print(year)

date_of_birth = dt.datetime(year=1994, month=7, day=13)
print(date_of_birth)
