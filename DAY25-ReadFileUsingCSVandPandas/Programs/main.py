with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY25-ReadFileUsingCSVandPandas/Resources/weather_data.csv') as data_file:
    data = data_file.readlines()
    print(data)


import csv

with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY25-ReadFileUsingCSVandPandas/Resources/weather_data.csv') as data_file:
    data = csv.reader(data_file)
    # it will return an object "<_csv.reader object at 0x000001C82A2F0BE0>"
    # print(data)
    temperature = []
    for row in data:
        print(row)
        if row[1] != 'temp':
            temperature.append(int(row[1]))

    print(temperature)


